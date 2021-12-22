<?php
/*
 * SMTP Email Sending
 * By Stewart Souter
 * Date Created: Thurs, 11 August 2011 17:15:37 GMT
 * Last Updated: Fri, 19 August 2011 10:54:35 GMT 
 * email: webmaster@carbonize.co.uk
 * 
 * By using this script you are agreeing to leave this
 * comment and agreement in place and untouched. If you
 * use any part of this code you must make it clear where
 * it came from and give credit where it is due.
 */

$mailCfg['Server']    = '';    // Servername
$mailCfg['User']      = '';    // SMTP username if needed
$mailCfg['Pass']      = '';    // SMTP Password if needed
$mailCfg['Port']      = 25;    // SMTP server port. 25 is the usual and 465 if using SSL
$mailCfg['popServer'] = '';    // Name of the pop server. Leave empty if POP Auth not required
$mailCfg['popPort']   = 110;   // Port for the pop server. 110 is the usual and 995 if using SSL
$mailCfg['SSL']       = 0;     // Does your SMTP server need you to use SSL or TLS? 0 = no, 1 = SSL, 2 = TLS

// This function delivers the email directly to the recipients mail server so bypassing the need for your own
function directMail($mailTo, $mailSubject, $mailMsg, $mailHeaders = '', $mailFrom = '', $mailCfg)
{
  if(empty($mailFrom))
  {
    return false; // No from address == no sending
  }
  $mailParts = explode('@', $mailTo);  // Seperate the parts of the email address
  @getmxrr($mailParts[1], $mxHosts, $mxWeight); // Get the MX records for the emails domain
  for($i=0;$i<count($mxHosts);$i++) // Put the records and weights into an array
  {
      $mxServers[$mxHosts[$i]] = $mxWeight[$i];
  }
  asort($mxServers); // Sort the array so they are in weighted order
  foreach($mxServers as $key => $value)
  {
    $mailCfg['Server'] = $key; // Set the SMTP server to the current MX record
    if(smtpMail($mailTo, $mailSubject, $mailMsg, $mailHeaders, $mailFrom, $mailCfg)) // Send the email using the MX server
    {
      return true;  // The email was successfully sent
    }
  }
  return false;  // Houston we have a problem
}

// This function connects to the SMTP server and does the AUTH if needed. Can also do a POP login if server requires that.
function smtpMail($mailTo, $mailSubject, $mailMsg, $mailHeaders = '', $mailFrom = '', $mailCfg )
{
  if(empty($mailFrom))
  {
    return false; // No from address == no sending
  }
  $timeout = '30'; // How long to keep trying to connect
  $localhost = 'localhost'; // How to identify ourselves
  $logArray = array(); // For storing the replies
  
  /* * * * POP Login if required * * */ 
  
  if(!empty($mailCfg['popServer'])) // Can't really do POP Auth without a server
  {
    $ssl = ($mailCfg['SSL'] != 0) ? (($mailCfg['SSL'] == 1) ? 'ssl://' : 'tls://') : ''; // If SSL or TLS add it
    $popConnect = @fsockopen($ssl.$mailCfg['popServer'], $mailCfg['popPort'], $errno, $errstr, $timeout); // Connect
    if(!$popConnect) // If we fail to connect...
    {
      $logArray['POPconnect'] = $errstr . '(' . $errno . ')'; // Log the given reason...
      logMailError($logArray); // And output to the log file.
      return false;
    }
    else
    {
      $logArray['POPconnect'] = @fgets($popConnect, 515)); // POP servers only return single line replies. Or should.
      if(!mailPackets('AUTH LOGIN', $popConnect, 'SMTPauth')) //Request Auth Login
      {
        return false;
      }
      if(!mailPackets('USER ' . $smtpUser, $popConnect, 'POPuser')) // Send username. POP is plaintext
      {
        return false;
      }    
      if(!mailPackets('PASS ' . $smtpPass, $popConnect, 'POPpass')) // Send password, again in plaintext
      {
        return false;
      }
      if(!mailPackets('QUIT', $popConnect, 'POPquit')) // Say bye to the server
      {
        return false;
      }    
      fclose($popConnect); // Close connection
    }
  }
  
  /* * * * End of POP Login * * * * */
  
  /* * * * Start of SMTP stuff * * * */
 
  $ssl = ($mailCfg['SSL'] != 0) ? (($mailCfg['SSL'] == 1) ? 'ssl://' : 'tls://') : ''; // Set the encryption if needed
  $smtpConnect = @fsockopen($ssl.$mailCfg['Server'], $mailCfg['Port'], $errno, $errstr, $timeout); // Connect
  if(!$smtpConnect) // If we fail to connect...
  {
    $logArray['SMTPconnect'] = $errstr . '(' . $errno . ')'; // Add the reason to the log...
    logMailError($logArray); // Then output the log
    return false;
  }
  else
  {
    $cnectKey = 0; // A counter for when we receive multiple lines in reply
    do
    {
      $smtpResponse = @fgets($smtpConnect, 515); // Get the reply
      $cnectKey++; // Increment the counter
      $logArray['SMTPconnect' . $cnectKey] = $smtpResponse; // Log the response
      $responseCode = substr($smtpResponse, 0, 3); // Grab the response code from start of the response
      // If we get an error terminate the connection and log the results so far
      if($responseCode >= 400)
      {  
        logMailError($logArray, $smtpConnect);
        return false;
      }        
    }  
    while((strlen($smtpResponse) > 3) && (strpos($smtpResponse, ' ') != 3)); // Loop until we get told it's the last line
      $ehlo = mailPackets('EHLO ' . $localhost, $smtpConnect, $logArray, 'SMTPehlo'); // Let's try using EHLO first
      if($ehlo != 250) // Server said it didn't like EHLO so drop back to HELO
      {
        if(!mailPackets('HELO ' . $localhost, $smtpConnect, $logArray, 'SMTPhelo')) // Send HELO. No EHLO means server doesn't support AUTH
        {
          return false;
        }
      }
      if(!empty($mailCfg['User']) && ($ehlo == 250)) // We have a username and server supports EHLO so send login credentials
      {
        if(!mailPackets('AUTH LOGIN', $smtpConnect, $logArray, 'SMTPauth')) // Request Auth Login
        {
          return false;
        }
        if(!mailPackets(base64_encode($mailCfg['User']), $smtpConnect, $logArray, 'SMTPuser')) // Send username
        {
          return false;
        }
        if(!mailPackets(base64_encode($mailCfg['Pass']), $smtpConnect, $logArray, 'SMTPpass')) // Send password
        {
          return false;
        }
      }
      if(!mailPackets('MAIL FROM:<' . $mailFrom . '>', $smtpConnect, $logArray, 'SMTPfrom')) // Email From
      {
        return false;
      }
      if(!mailPackets('RCPT TO:<' . $mailTo . '>', $smtpConnect, $logArray, 'SMTPrcpt')) // Email To
      {
        return false;
      }
      if(!mailPackets('DATA', $smtpConnect, $logArray, 'SMTPmsg')) // We are about to send the message
      {
        return false;
      }
      // First lets make sure both the message and additional headers do not contain anythign that might be seen as end of message marker
      $mailMsg = preg_replace(array("/(?<!\r)\n/", "/\r(?!\n)/", "/\r\n\./"), array("\r\n", "\r\n", "\r\n.."), $mailMsg);
      $mailHeaders = (!empty($mailHeaders)) ? "\r\n" . preg_replace(array("/(?<!\r)\n/", "/\r(?!\n)/", "/\r\n\./"), array("\r\n", "\r\n", "\r\n.."), $mailHeaders) : '';
      // Create the default headers, attach any additonal headers
      $mailHeaders = "To: <".$mailCfg['To'].">\r\nFrom: <".$mailCfg['From'].">\r\nSubject: ".$mailCfg['Subject']."\r\nDate: " . gmdate('D, d M Y H:i:s') . " -0000".$mailHeaders;
      if(!mailPackets($mailHeaders."\r\n\r\n".$mailMsg."\r\n.", $smtpConnect, $logArray, 'SMTPbody')) // The message
      {
        return false;
      }
      mailPackets('QUIT', $smtpConnect, $logArray, 'SMTPquit'); // Say Bye to SMTP server
      fclose($smtpConnect); // Be nice and close the connection
      return true; // Return the fact we sent the message
  }
}

// This function sends the actual packets then logs the reponses and parses the reponse code
function mailPackets($sendStr,$mailConnect,&$logArray,$logName = '')
{
  $newLine = "\r\n"; // LEAVE THIS ALONE  
  $keyCount = 0;  // Just an incremental counter for when we get more than a single line response
  @fputs($mailConnect,$sendStr . $newLine); // Send the packet 
  do // Start grabbing the responses until we either get a terminal error or told we are at the end
  {
    $mailResponse = @fgets($mailConnect, 515); // Receive the response
    $keyCount++; // Incrememnt the key count
    $logArray[$logName . $keyCount] = $mailResponse; // Put the response in to the log array
    $responseCode = substr($smtpResponse, 0, 3); // Grab the response code from start of the response
    // Check for error codes except on ehlo, auth, and user details as they are not always fatal
    if((($logName != 'SMTPauth') && ($logName != 'SMTPuser') && ($logName != 'SMTPehlo') && ($logName != 'SMTPpass')) && ($responseCode >= 400))
    {  
       logMailError($logArray,$mailConnect);
       return false;
    }
    elseif((substr($responseCode, 0, 1) == 4) || ($responseCode >= 521) && ($logName != 'SMTPehlo'))
    {  
       logMailError($logArray,$mailConnect);
       return false;
    }
  }
  while((strlen($mailResponse) > 3) && (strpos($mailResponse, ' ') != 3)); // Loop until we get the end response
  return $responseCode; // Return the response code
}

function logMailError(&$logArray, $mailServer = false)
{
  if($mailServer)
  { 
    fclose($mailServer); // Be nice and close the connection
  }
  $fd = @fopen ('smtplog.txt', 'a'); // open the log file
  $mailResults = print_r($logArray, true); // Create a nice printable version of logArray
  @fwrite($fd,$mailResults); // Write the log
  @fclose ($fd); // Close the file
}

?>