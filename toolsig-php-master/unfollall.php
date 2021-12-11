<?php
include 'class_ig.php';
error_reporting(0);
clear();
echo "
Ξ TITLE  : UNFOLLOW ALL FOLLOWING
Ξ FLPATH : tools/unfollall.php
Ξ CODEBY : Firdy [https://fb.com/6null9]
Ξ FIXBY	 : Andi Muh. Rizqi [ikiganteng]
Ξ UPDATE : Officialputuid [26/01/2020]

";
$u = getUsername();
$p = getPassword();
echo PHP_EOL;
$sleep = getComment('[?] Sleep in Seconds: ');
echo '•••••••••••••••••••••••••••••••••••••••••' . PHP_EOL . PHP_EOL;
$login = login($u, $p);
if ($login['status'] == 'success') {
	
	echo color()["LG"].'[*] Login as '.$login['username'].' Success!' . PHP_EOL;
	$data_login = array(
		'username' => $login['username'],
		'csrftoken'	=> $login['csrftoken'],
		'sessionid'	=> $login['sessionid']
	);
	
	$data_target = findProfile($u, $data_login);
	echo color()["LG"].'[#] Name: '.$data_target['fullname'].' | Followers: '.$data_target['followers'] .' | Following: '.$data_target['following'] . PHP_EOL;
	if ($data_target['status'] == 'success') {

		$cmt = 0;
		for ($i=1; $i < $data_target['following']; $i++) { 

			$profile = getFollowing($u , $data_login, $i, 1);
			foreach ($profile as $rs) {

				$username = $rs->username;
				$unfollow = unfollow($username, $data_login);
				if ($unfollow['status'] == 'success') {
					
					echo color()["LG"].'[>] Unfollow "'.$username.'" Success!';
					sleep($sleep);
					echo PHP_EOL;
				}else{

					echo color()["LR"].'[!] Unfollow "'.$username.'" Failed!';
					sleep($sleep);
					echo PHP_EOL;
				}

			}

		}

	}else{

		echo 'Error!';
		echo PHP_EOL;
	}
}else{

	echo color()["LR"].'[*] Login as '.$login['username'].' Failed!' . PHP_EOL;
}
