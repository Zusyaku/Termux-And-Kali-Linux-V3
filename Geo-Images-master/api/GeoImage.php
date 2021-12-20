<?php
/*
Using this function, you can scan
geo location from images. You can
also using the official website
in https://tool.geoimgr.com. Thanks
to https://github.com/rasitech-sudo
for your request😃.


Source: https://github.com/Kotzyy
*/
function Scan($path, $isArray = false)
    {
    $ch = curl_init('https://tool.geoimgr.com/upload');
    curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 0,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => 'POST',
    CURLOPT_POSTFIELDS => [
        'upfile'=>  new CURLFile(
            realpath($path)
        )
        ]
    ]);
    $response = curl_exec($ch);
    if (curl_errno($ch)) {
        return false;
    } else {
        return $isArray ? json_decode($response) : $response;
    }
    curl_close($ch);
}
function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}