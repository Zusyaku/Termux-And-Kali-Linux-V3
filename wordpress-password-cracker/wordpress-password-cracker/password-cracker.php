<?php
/*
Plugin Name: WordPress Password Cracker
Plugin URI: http://www.freecharity.org.uk/wordpress-password-cracker/
Description: Password auditor for WordPress user accounts.
Version: 1.0
Author: James Davis
Author URI: http://www.freecharity.org.uk/
*/
function fcpassword_passwordStrength($password,$username){
	if(strlen($password) < 4) return 1;
	if(strtolower($password) == strtolower($username)) return 2;
	$symbolspace = 0;
	if(preg_match('/[0-9]/',$password)) $symbolspace += 10;
	if(preg_match('/[a-z]/',$password)) $symbolspace += 26;
	if(preg_match('/[A-Z]/',$password)) $symbolspace += 26;
	if(preg_match('/[^a-zA-Z0-9]/',$password)) $symbolspace += 31;
	$natlog = log(pow($symbolspace,strlen($password)));
	$score = $natlog / M_LN2;
	if($score < 40) return 2;
	if($score < 56) return 3;
	return 4;
}

$nhashes = 0;
$ntime = microtime(TRUE);

require_once( ABSPATH . 'wp-includes/class-phpass.php');



function fcpassword_checkPasswords () {
	global $wpdb;
	global $table_prefix;
	
	$hasher = new PasswordHash(8, TRUE);
	$ntime = microtime(TRUE);
	
	$user_table = $table_prefix . "users";
	$sql = "select user_login,user_pass from $user_table;";

	$filename = str_replace(basename( __FILE__),"",plugin_basename(__FILE__))."dictionary.txt";
	$handle = @fopen($filename,"r");

	foreach($wpdb->get_results($sql) as $row){
		$username = $row->user_login;
		$hash = $row->user_pass;
		$text .= "<i>Checked Username: $username</i>"."<br/>";
		while(!feof($handle)){
			$password  = rtrim(fgets($handle));
			if($hasher->CheckPassword($password,$hash)){
				$text .= "<strong>FOUND</strong> Username: $username Password: $password\n"."<br/>";
			} else {
			
			}
			$nhashes++;
		}
		rewind($handle);
	}
	fclose($handle);
	$text .= sprintf("<i>Checked %d passwords in %f seconds (%.2f pass/sec)</i>",$nhashes,microtime(TRUE)-$ntime,$nhashes/(microtime(TRUE)-$ntime));
	$nhashes = 0;
	return $text;
}

add_action('admin_menu', 'fcpassword_add_pages'); 

function fcpassword_add_pages() {
	add_submenu_page("tools.php", "Password Cracker", "Password Cracker", 10,basename(__FILE__)."_main", 'fcpassword_main_page'); 
}

function fcpassword_background(){
	update_option('fcpassword', fcpassword_checkPasswords());
	update_option('fcpassword_status','Completed');
}
add_action('fcpassword_cronevent','fcpassword_background');

function fcpassword_main_page(){
	if($_POST['go'] == 'yes'){
		?>
			<div id="message" class="updated fade"><p><strong>				
				New run started in background
			</strong></p></div>
		<?php
		wp_schedule_single_event(time()-1, 'fcpassword_cronevent');
		update_option('fcpassword','');
		update_option('fcpassword_status','Running...');
		spawn_cron(time());
	}
?>
<div class='wrap'>
	<h2>WordPress Password Cracker</h2>
	<p>
		This plugin compares a list of passwords against the user accounts in a WordPress blog, using the password hashing functions built into WordPress. It can be a useful tool for auditing your user's choice of passwords. This plugin uses no functions or data not already available to other plugins, or administrators.
	</p>
	<p>
		The password dictionary is stored in 'dictionary.txt' in the plugin's home directory. A small sample dictionary of common passwords is included. The check is run in the background: due to the secure hashing algorithm large dictionaries may take a <strong>long</strong> time to check. Use the sample dictionary to guage the performance of a more thorough check.
	</p>
</div>

<?php if(get_option('fcpassword') != "") { ?>
<div class='wrap'>
	<h2>Results:</h2>
	<p>
		<?php echo get_option('fcpassword'); ?><br/> 
	</p>
</div>
<?php 
	} 
?>
<div class='wrap'>
	<p>
		Status: <?php echo get_option('fcpassword_status'); ?><br/>
	</p>
	<?php
		if (get_option('fcpassword_status')!='Running...') {
	?>
	<form name = "clicky" method="post" action="<?php echo str_replace( '%7E', '~', $_SERVER['REQUEST_URI']); ?>">
		<input type='hidden' name='go' value='yes'/>
		<input type='submit' name='Submit' value='Run cracker'/>
	</form>
	<?php 
		} else { 
	?>
			<a href="<?php echo str_replace( '%7E', '~', $_SERVER['REQUEST_URI']); ?>">Refresh</a>
	<?php
		}
	?>
</div>
<?php
}

?>
