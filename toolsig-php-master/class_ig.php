<?php

define("OS", strtolower(PHP_OS));
header('Content-Type: text/html; charset=utf-8');
error_reporting(0);
function getStr($string,$start,$end){
    $str = explode($start,$string);
    $str = explode($end,$str[1]);
    return $str[0];
}

function RandStr($randstr){ 
    $char = 'qwertyuiopasdfghjklzxcvbnm';
    $char .= 'QWERTYUIOPASDFGHJKLZXCVBNM'; 
    $char .= '0123456789'; 

    $str = ''; 
    for ($i = 0; $i < $randstr; $i++ ) { 
        $pos = rand(0, strlen($char)-1); 
        $str .= $char{$pos}; 
    } 
    return $str; 
}
function RandInt($randstr){ 
    $char = '0123456789'; 
    $str = ''; 
    for ($i = 0; $i < $randstr; $i++ ) { 
        $pos = rand(0, strlen($char)-1); 
        $str .= $char{$pos}; 
    } 
    return $str; 
}

/* function copycat()
{

    ## Official Copyright by Firdy [https://fb.com/6null9] ##
 
    $data = 'IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiAKIC8kJCQkJCQgIC8kJCQkJCQgIC8kJCQkJCQkJCAgICAgICAgICAgICAgICAgIC8kJCAgICAgICAgICAKfF8gICQkXy8gLyQkX18gICQkfF9fICAkJF9fLyAgICAgICAgICAgICAgICAgfCAkJCAgICAgICAgICAKICB8ICQkICB8ICQkICBcX18vICAgfCAkJCAgLyQkJCQkJCAgIC8kJCQkJCQgfCAkJCAgLyQkJCQkJCQKICB8ICQkICB8ICQkIC8kJCQkICAgfCAkJCAvJCRfXyAgJCQgLyQkX18gICQkfCAkJCAvJCRfX19fXy8KICB8ICQkICB8ICQkfF8gICQkICAgfCAkJHwgJCQgIFwgJCR8ICQkICBcICQkfCAkJHwgICQkJCQkJCAKICB8ICQkICB8ICQkICBcICQkICAgfCAkJHwgJCQgIHwgJCR8ICQkICB8ICQkfCAkJCBcX19fXyAgJCQKIC8kJCQkJCR8ICAkJCQkJCQvICAgfCAkJHwgICQkJCQkJC98ICAkJCQkJCQvfCAkJCAvJCQkJCQkJC8KfF9fX19fXy8gXF9fX19fXy8gICAgfF9fLyBcX19fX19fLyAgXF9fX19fXy8gfF9fL3xfX19fX19fLyAKICAgIApNYWRlIHdpdGggTG92ZSA8MyBDb2RlIGJ5IEZpcmR5CiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw==';

    echo base64_decode($data).PHP_EOL;
}
*/

function curl($url, $data = 0, $header = 0, $cookie = 0) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    // curl_setopt($ch, CURLOPT_VERBOSE, 1);
    curl_setopt($ch, CURLOPT_HEADER, 1);
    if($header) {
        curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
        curl_setopt($ch, CURLOPT_ENCODING, "gzip");
    }
    if($data) {
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    }
    if($cookie) {
        curl_setopt($ch, CURLOPT_COOKIEJAR, $cookie);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $cookie);
    }
    $x = curl_exec($ch);
    curl_close($ch);
    return $x;
}

function curlNoHeader($url, $data = 0, $header = 0, $cookie = 0) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);

    curl_setopt($ch, CURLOPT_HEADER, 0);
    if($header) {
        curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
        curl_setopt($ch, CURLOPT_ENCODING, "gzip");
    }
    if($data) {
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    }
    if($cookie) {
        curl_setopt($ch, CURLOPT_COOKIEJAR, $cookie);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $cookie);
    }
    $x = curl_exec($ch);
    curl_close($ch);
    return $x;
}

function color() {
    return [
        "LW" => (OS == "linux" ? "\e[1;37m" : ""),
        "WH" => (OS == "linux" ? "\e[0m" : ""),
        "LR" => (OS == "linux" ? "\e[1;31m" : ""),
        "LG" => (OS == "linux" ? "\e[1;32m" : ""),
        "BL" => (OS == "linux" ? "\e[1;34m" : ""),
        "MG" => (OS == "linux" ? "\e[1;35m" : ""),
        "LC" => (OS == "linux" ? "\e[1;36m" : ""),
        "CY" => (OS == "linux" ? "\e[1;33m" : "")
    ];
}

function clear(){

    return (OS == "linux" ? system('clear') : "" );

}

function fetchCurlCookies($source) {
    preg_match_all('/^Set-Cookie:\s*([^;]*)/mi', $source, $matches);
    $cookies = array();
    foreach($matches[1] as $item) {
        parse_str($item, $cookie);
        $cookies = array_merge($cookies, $cookie);
    }
    return $cookies;
}


function findProfile($username, $session = 0)
{
    $url = 'https://instagram.com/'.$username;
    if ($session != 0) {
        $header = array();
        $header[] = 'Cookie: sessionid='.$session['sessionid'].';';
        $get = curl($url,0,$header);

    }else{

        $get = curl($url);
    }
    if (strpos($get, 'The link you followed may be broken, or the page may have been removed.')) {

        $data = array(
            'status' => 'error',
            'details' => 'user not found'
        );
    
    }else{

        $data_ouput = getStr($get, '<script type="text/javascript">window._sharedData = ', ';</script>');
        $data_array = json_decode($data_ouput);
        $result = $data_array->entry_data->ProfilePage['0']->graphql->user;
        if (empty($result->edge_owner_to_timeline_media->edges) && $result->edge_owner_to_timeline_media->count >= 1) {
            
            $data = array(
                'status' => 'error',
                'details' => 'account private'
            );

        }else{

            $result = $data_array->entry_data->ProfilePage['0']->graphql->user;
            // $vid = ($result->is_video == 1) ? "yes" : "no" ;
            $is_follow = ($result->followed_by_viewer) ? 'true' : 'false' ;
            $is_private = ($result->is_private) ? 'true' : 'false' ;
            $is_verified = ($result->is_verified) ? 'true' : 'false' ;
            $is_polbek = ($result->follows_viewer) ? 'true' : 'false' ;

            $data = array(
                'status' => 'success',
                'username' => $username,
                'fullname' => $result->full_name,
                'followers' => $result->edge_followed_by->count,
                'following' => $result->edge_follow->count,
                'is_follow' => $is_follow,
                'is_private' => $is_private,
		'is_polbek' => $is_polbek,
                'id' => $result->id,
                'is_verif' => $is_verified,
                'post' => $result->edge_owner_to_timeline_media->count,
            );
            
        }
    }
    
    return $data;
}

function getProfile($session)
{
    $url = 'https://www.instagram.com/accounts/edit/?__a=1';
    $header = array(
        'Cookie: sessionid='.$session['sessionid'].';',
    );

    $get = curl($url,0,$header);

    $first_name = getStr($get, '{"first_name":"', '","');
    $last_name = getStr($get, '"last_name":"', '","');
    $email = getStr($get, 'email":"', '","');
    $username = getStr($get, '"username":"', '","');
    $bio = getStr($get, 'biography":"', '","');

    $data = array(
        'first_name' => $first_name,
        'last_name' => $last_name,
        'email' => $email,
        'username' => $username,
        'bio' => $bio,
    );

    return $data;
}


function login($username, $password)
{
    ## URL ##
    $url_login = 'https://www.instagram.com/accounts/login/ajax/';
    $url_ig = 'https://www.instagram.com/accounts/login/';

    ## GET COOKIE SEBELUM LOGIN ##
    $get = curl($url_ig);
    $cookie = fetchCurlCookies($get);
    $csrf = $cookie['csrftoken'];
    $mid = $cookie['mid'];

    ## HEADER LOGIN ##
    $header = array(
        'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
        'X-CSRFToken: '.$csrf,
        'Content-Type: application/x-www-form-urlencoded',
        'Cookie: rur=FTW; mid='.$mid.'; csrftoken='.$csrf.'',
    );

    ## BODY LOGIN ##
    $body = 'username='.$username.'&password='.$password.'&queryParams=%7B%7D&optIntoOneTap=false';

    ## LOGIN ##
    $post = curl($url_login, $body, $header);

    if (strpos($post, '{"authenticated": false')) {
        
        $data = array(
            'action' => 'login',
            'status' => 'error',
            'username' => $username, 
        );

    }elseif(strpos($post, '{"authenticated": true')){

        $cookie_log = fetchCurlCookies($post);
        $data = array(

            'action' => 'login',
            'status' => 'success',
            'username' => $username, 
            'csrftoken' => $cookie_log['csrftoken'],
            'sessionid' => $cookie_log['sessionid'],
        );

    }else{

        $data = $post;
    }

    return $data;

}

function comment($id, $session, $text)
{
    $url = 'https://www.instagram.com/web/comments/'.$id.'/add/';
    $header = array(
            'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
            'X-CSRFToken: '.$session['csrftoken'],
            'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
        );
    $body = 'comment_text='.$text.'&replied_to_comment_id=';
    $post = curlNoHeader($url,$body,$header);
    $result = json_decode($post);
    if (strpos($post, 'Please wait')) {
        
        $data = array(
            'action' => 'comment',
            'status' => 'error',
            'details' => 'Please wait a few minutes before you try again'
        );

    }elseif (strpos($post, '"status": "ok"')) {

        $data = array(
            'action' => 'comment',
            'status' => 'success',
            'text' => $result->text
        );

    }else{

        $data = array(
            'action' => 'comment',
            'status' => 'error',
            'details' => $post
        );
    }


    return $data;
}


function like($id, $session)
{
    if (isset($id)) {
        $url = 'https://www.instagram.com/web/likes/'.$id.'/like/';
        $header = array(
                'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
                'X-CSRFToken: '.$session['csrftoken'],
                'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
            );
        $post = curl($url,1,$header);

        $data = (strpos($post, "Error")) ? array("media" => $id, "action" => "like", "status" => "error") : array("media" => $id, "action" => "like", "status" => "success");
    }else{

        $data = array("media" => $id, "status" => "error", "details" => "media not found");
    }
    
    return $data;
}


function unlike($id, $session)
{
    if (isset($id)) {
        $url = 'https://www.instagram.com/web/likes/'.$id.'/unlike/';
        $header = array(
                'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
                'X-CSRFToken: '.$session['csrftoken'],
                'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
            );
        $post = curl($url,1,$header);

        $data = (strpos($post, "Error")) ? array("media" => $id, "action" => "unlike", "status" => "error") : array("media" => $id, "action" => "unlike", "status" => "success");
    }else{

        $data = array("media" => $id, "status" => "error", "details" => "media not found");
    }
    
    return $data;
}


function unfollow($username, $session)
{
    $profile = findProfile($username);
    if (isset($profile['id'])) {
        $id = $profile['id'];
        $url = 'https://www.instagram.com/web/friendships/'.$id.'/unfollow/';
        $header = array(
                'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
                'X-CSRFToken: '.$session['csrftoken'],
                'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
            );
        $post = curl($url,1,$header);

        $data = (strpos($post, "Error")) ? array("username" => $username, "action" => "unfollow", "status" => "error") : array("username" => $username, "action" => "unfollow", "status" => "success");
    }else{

        $data = array("username" => $username, "status" => "error", "details" => "username not found");
    }
    
    return $data;
}


function follow($username, $session)
{
    $profile = findProfile($username, $session);
    if (isset($profile['id'])) {

        $id = $profile['id'];
        $url = 'https://www.instagram.com/web/friendships/'.$id.'/follow/';
        $header = array(
                'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
                'X-CSRFToken: '.$session['csrftoken'],
                'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
            );
        if ($profile['is_follow'] == 'true') {
            
            $data = array(
                'status' => 'error',
                'details' => 'already follow'
            );
        }else{

            $post = curl($url,1,$header);
			$data_ouput = getStr($post, '<script type="text/javascript">window._sharedData = ', ';</script>');
			$data_array = json_decode($data_ouput);
			$result = $data_array->entry_data->ProfilePage['0']->graphql->user;
			$is_follow = ($result->followed_by_viewer) ? 'true' : 'false' ;
            if (strpos($post, 'Location: https://www.instagram.com/accounts/login/') && strpos($post, '302 Found')) {
                
                $data = array(
                    'status' => 'error',
                    'details' => 'you are note logged in'
                );
            }elseif ($is_follow == 'true') {
                
                $data = array(
                    'username' => $username,
                    'action' => 'follow',
                    'status' => 'success',
                );
            }else{
			$a = getStr($post, '{', '}');
			$b = '{'.$a.'}';

                $data = array(
                    'username' => $username,
                    'action' => 'follow',
                    'status' => 'error',
                    'details' => $b,
                );
            }
        }

    }else{

        
        $data = array(
            'status' => 'error',
            'username' => $username,
            'action' => 'follow',
            'details' => 'username not found',
        );
    }

    return $data;
}

function followById($id, $session)
{
    $url_info = 'https://i.instagram.com/api/v1/users/'.$id.'/info/';
    $info = curlNoHeader($url_info);
    $data_info = json_decode($info);
    $username = $data_info->user->username;

    if (strpos($info, 'Page Not Found')) {

        $data = array(
            'status' => 'error',
            'username' => $username,
            'action' => 'follow',
            'details' => 'username not found',
        );
        
    }else{

        $url = 'https://www.instagram.com/web/friendships/'.$id.'/follow/';
        $header = array(
                'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
                'X-CSRFToken: '.$session['csrftoken'],
                'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
            );

        $post = curl($url,1,$header);
        if (strpos($post, 'Location: https://www.instagram.com/accounts/login/') && strpos($post, '302 Found')) {
            
            $data = array(
                'status' => 'error',
                'details' => 'you are note logged in'
            );
        }elseif (strpos($post, 'Location: https://www.instagram.com/'.$username) && strpos($post, '302 Found')) {
            
            $data = array(
                'username' => $username,
                'action' => 'follow',
                'status' => 'success',
            );

        }elseif($profile['is_follow'] == 'true'){

            $data = array(
                'username' => $username,
                'action' => 'follow',
                'status' => 'error',
                'details' => 'already follow',
            );
        }else{

            $data = array(
                'username' => $username,
                'action' => 'follow',
                'status' => 'error',
                'details' => 'unexpected error',
            );
        }
    }

    return $data;

}

function block($username, $session)
{
    $profile = findProfile($username);
    if (isset($profile['id'])) {
        $id = $profile['id'];
        $url = 'https://www.instagram.com/web/friendships/'.$id.'/block/';
        $header = array(
                'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
                'X-CSRFToken: '.$session['csrftoken'],
                'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
            );

        $post = curl($url,1,$header);
        $data = (strpos($post, '{"status": "ok"}')) ? array("username_target" => $username, "action" => "block", "status" => "success") : array("username_target" => $username, "action" => "block", "status" => "error");
    }else{

        $data = array("username" => $username, "status" => "error", "details" => "username not found");
    }
    
    return $data;
}

function unblock($username, $session)
{
    $profile = findProfile($username);
    if (isset($profile['id'])) {
        $id = $profile['id'];
        $url = 'https://www.instagram.com/web/friendships/'.$id.'/unblock/';
        $header = array(
                'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
                'X-CSRFToken: '.$session['csrftoken'],
                'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
            );

        $post = curl($url,1,$header);
        $data = (strpos($post, '{"status": "ok"}')) ? array("username_target" => $username, "action" => "unblock", "status" => "success") : array("username_target" => $username, "action" => "unblock", "status" => "error");
    }else{

        $data = array("username" => $username, "status" => "error", "details" => "username not found");
    }
    
    return $data;
}

function deletePost($id, $session)
{
    $data = array();
    $url = 'https://www.instagram.com/create/'.$id.'/delete/';
    $header = array(
            'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
            'X-CSRFToken: '.$session['csrftoken'],
            'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
        );
    $delete = curl($url,1,$header);
    if (strpos($delete, 'This page could not be loaded.')) {
        
        $data['status'] = 'error';
        $data['details'] = 'make sure you already login'; 
    }elseif (strpos($delete, '{"did_delete": true, "status": "ok"}')) {
        
        $data['status'] = 'success';
        $data['action'] = 'delete';
        $data['id'] = $id;
    }else{

        $data['status'] = 'error';
        $data['details'] = 'unexpected error, please contact Admin'; 

    }

    return $data;
}

function getPassword($prompt = "[?] Enter Password: ") {

    echo $prompt;
    $password = trim(fgets(STDIN));
    
    return $password;
    
}

function getUsername($prompt = "[?] Enter Username: ") {
    echo $prompt;

    $username = trim(fgets(STDIN));

    return $username;
}

function getComment($prompt = "[?] Enter Comment Text: ") {
    echo $prompt;

    $text = trim(fgets(STDIN));

    return $text;
}

function getFollowingLink($username, $count, $after = '')
{

    $profile = findProfile($username);
    if (isset($profile['id'])) {

        $accountId = $profile['id'];
        $url_folls = 'https://www.instagram.com/graphql/query/?query_id=17874545323001329&id={{accountId}}&first={{count}}&after={{after}}';
        $url = str_replace('{{accountId}}', urlencode($accountId), $url_folls);
        $url = str_replace('{{count}}', urlencode($count), $url);
        if ($after === '') {
            $url = str_replace('&after={{after}}', '', $url);
        } else {
            $url = str_replace('{{after}}', urlencode($after), $url);
        }

    }else{

        $url = '';
    }
    
    return $url;
}

function getFollowersLink($username, $count, $after = '')
{

    $profile = findProfile($username);
    if (isset($profile['id'])) {

        $accountId = $profile['id'];
        $url_folls = 'https://www.instagram.com/graphql/query/?query_id=17851374694183129&id={{accountId}}&first={{count}}&after={{after}}';
        $url = str_replace('{{accountId}}', urlencode($accountId), $url_folls);
        $url = str_replace('{{count}}', urlencode($count), $url);
        if ($after === '') {
            $url = str_replace('&after={{after}}', '', $url);
        } else {
            $url = str_replace('{{after}}', urlencode($after), $url);
        }

    }else{

        $url = '';
    }
    
    return $url;
}

function getFollowers($username, $login, $count = 20, $pageSize = 20)
{
    $index = 0;
    $accounts = [];
    $endCursor = '';
    $header = array();
    $header[] = 'Cookie: sessionid='.$login['sessionid'].';';
    if ($count < $pageSize) {

        echo 'Count must be greater than or equal to page size.'.PHP_EOL;
    }
    while (true) {

        $url = getFollowersLink($username, 20, $endCursor);
        
        if ($url != '') {
            
            $response = curlNoHeader($url, 0, $header);
        }

        $data = json_decode($response);
        $pageInfo = $data->data->user->edge_followed_by;

        if ($pageInfo->count == 0) {
            
            return $accounts;
        }
        if ($pageInfo->edges == 0) {
            
            echo 'Failed to get followers of ' . $username . '. The account is private.';
        }

        foreach ($pageInfo->edges as $edge) {
            $accounts[] = $edge->node;
            $index++;
            if ($index >= $count) {
                break 2;
            }
        }

        if ($pageInfo->page_info->has_next_page) {
           
            $endCursor = $pageInfo->page_info->end_cursor;
        
        } else {
            
            $endCursor = '';
            break;
        }
    }

    return $accounts;
}

function getFollowing($username, $login, $count = 20, $pageSize = 20)
{
    $index = 0;
    $accounts = [];
    $endCursor = '';
    $header = array();
    $header[] = 'Cookie: sessionid='.$login['sessionid'].';';
    if ($count < $pageSize) {

        echo 'Count must be greater than or equal to page size.'.PHP_EOL;
    }
    while (true) {

        $url = getFollowingLink($username, 20, $endCursor);
        
        if ($url != '') {
            
            $response = curlNoHeader($url, 0, $header);
        }

        $data = json_decode($response);
        $pageInfo = $data->data->user->edge_follow;

        if ($pageInfo->count == 0) {
            
            return $accounts;
        }
        if ($pageInfo->edges == 0) {
            
            return 'Failed to get followers of ' . $username . '. The account is private.';
        }

        foreach ($pageInfo->edges as $edge) {
            $accounts[] = $edge->node;
            $index++;
            if ($index >= $count) {
                break 2;
            }
        }

        if ($pageInfo->page_info->has_next_page) {
           
            $endCursor = $pageInfo->page_info->end_cursor;
        
        } else {
            
            $endCursor = '';
            break;
        }
    }

    return $accounts;
}

function getAccountMediasJsonLink($variables)
{
    return str_replace('{variables}', urlencode($variables), 'https://www.instagram.com/graphql/query/?query_hash=42323d64886122307be10013ad2dcc44&variables={variables}');
}

function getMedias($username, $login, $count = 0, $maxId = '')
{
    $findProfile = findProfile($username);
    $id = $findProfile['id'];
    $index = 0;
    $medias = [];
    $isMoreAvailable = true;
    $header = array();
    $header[] = 'Cookie: sessionid='.$login['sessionid'].';';
    while ($index < $count && $isMoreAvailable) {
        $variables = json_encode([
            'id' => (string)$id,
            'first' => (string)$count,
            'after' => (string)$maxId
        ]);

        $url = getAccountMediasJsonLink($variables);
        $response = curlNoHeader($url, 0, $header);

        $obj = json_decode($response);
        $nodes = $obj->data->user->edge_owner_to_timeline_media->edges;
        // fix - count takes longer/has more overhead
        if (!isset($nodes) || empty($nodes)) {
            return [];
        }
        
        foreach ($nodes as $mediaObject) {
            if ($index === $count) {
                return $medias;
            }
            $medias[] = $mediaObject->node;
            $index++;
        }
        if (empty($nodes) || !isset($nodes)) {
            return $medias;
        }
        $maxId = $obj->data->user->edge_owner_to_timeline_media->page_info->end_cursor;
        $isMoreAvailable = $obj->data->user->edge_owner_to_timeline_media->page_info->has_next_page;
    }
    return $medias;
}

function getMedia($username, $login, $no)
{
    $media = getMedias($username, $login, $no);
    $dataObj = $media[$no-1];
    if ($dataObj) {
        
        $vid = ($dataObj->is_video == 1) ? "yes" : "no" ;
        $data = array(
            'status' => 'success',
            'id' => $dataObj->id,
            'page' => 'https://instagram.com/p/'.$dataObj->shortcode,
            'comments' => $dataObj->edge_media_to_comment->count,
            'likes' => $dataObj->edge_media_preview_like->count,
            'url_display' => $dataObj->display_url,
            'is_video' => $vid
        );
    }else{

        $data = array(
            'status' => 'error',
            'details' => 'Media Not Found.'
        );
    }

    return $data;
}

function getPost($username, $session = 0, $no = 0)
{
    $url = 'https://instagram.com/'.$username;
    if (!$session == 0) {

        $header = array(
            'Cookie: sessionid='.$session['sessionid'].';',
        );
        $get = curl($url,0,$header);

    }else{

        $get = curl($url);
    }
    
    if (strpos($get, 'The link you followed may be broken, or the page may have been removed.')) {

        $data = array(
            'status' => 'error',
            'details' => 'user not found'
        );
    
    }else{

        $data_ouput = getStr($get, '<script type="text/javascript">window._sharedData = ', ';</script>');
        $data_array = json_decode($data_ouput);
        $result = $data_array->entry_data->ProfilePage['0']->graphql->user->edge_owner_to_timeline_media->edges;
        if (empty($result) && $data_array->entry_data->ProfilePage['0']->graphql->user->edge_owner_to_timeline_media->count >= 1) {
            
            $data = array(
                'status' => 'error',
                'details' => 'account private'
            );

        }elseif ($data_array->entry_data->ProfilePage['0']->graphql->user->edge_owner_to_timeline_media->count <= 0) {
            
            $data = array(
                'status' => 'error',
                'details' => 'no post'
            );

        }else{

            $result = $data_array->entry_data->ProfilePage['0']->graphql->user->edge_owner_to_timeline_media->edges[$no]->node;
            $vid = ($result->is_video == 1) ? "yes" : "no" ;
        
            $data = array(
                'status' => 'success',
                'id' => $result->id,
                'page' => 'https://instagram.com/p/'.$result->shortcode,
                'comments' => $result->edge_media_to_comment->count,
                'likes' => $result->edge_liked_by->count,
                'url_display' => $result->display_url,
                'is_video' => $vid
            );
            
        }
    }

    return $data;
}

function activity($session)
{
        $url = 'https://www.instagram.com/accounts/activity/';
        $header = array(
                'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
                'X-CSRFToken: '.$session['csrftoken'],
                'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
            );
            $post = curl($url,1,$header);
			$data_ouput = getStr($post, '<script type="text/javascript">window._sharedData = ', ';</script>');
            $data_array = json_decode($data_ouput);
			$result = $data_array->entry_data->ActivityFeed['0']->graphql->user->activity_feed->edge_web_activity_feed;
			foreach ($result->edges as $items) {
			$data[] = array(
                'status' => 'success',
                'username' => $items->node->user->username,
                'type' => $items->node->type,
                'text' => $items->node->text,
            );
			}
    return $data;
}

function getHome($session)
{
        $url = 'https://www.instagram.com/';
        $header = array(
                'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
                'X-CSRFToken: '.$session['csrftoken'],
                'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
            );
            $post = curl($url,1,$header);
			$data_ouput = getStr($post, "window.__additionalDataLoaded('feed',", ");</script>");
            $data_array = json_decode($data_ouput);
			$result = $data_array->user->edge_web_feed_timeline;
			foreach ($result->edges as $items) {
			$data[] = array(
                'status' => 'success',
                'username' => $items->node->owner->username,
                'id' => $items->node->id,
                'link' => 'https://instagram.com/p/'.$items->node->shortcode,
                'text' => $items->node->edge_media_to_caption->edges[0]->node->text
			);
			}
    return $data_ouput;
}

function onetap($session)
{
        $url = 'https://www.instagram.com/accounts/onetap/?next=%2F';
        $header = array(
                'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
                'X-CSRFToken: '.$session['csrftoken'],
                'Cookie: csrftoken='.$session['csrftoken'].'; sessionid='.$session['sessionid']
            );
            $post = curl($url,1,$header);
			$data_ouput = getStr($post, '<script type="text/javascript">window._sharedData = ', ';</script>');
            $data_array = json_decode($data_ouput);
			$result = $data_array->config->viewer;
			$data = array(
                'status' => 'success',
                'name' => $result->full_name,
                'username' => $result->username,
            );
    return $data;
}
