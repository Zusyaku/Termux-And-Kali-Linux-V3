#!/usr/bin/python3
#coding=utf-8

"""

Copyright © 2021 - 2023 | Latip176 and Yayan XD
Semua codingan dibuat oleh Latip176. and Yayan XD

"""

import requests as req, json, time

tampung = []
hitung = 0

P = "\x1b[0;97m" 
M = "\x1b[0;91m"
H = "\x1b[0;92m"
K = "\x1b[0;93m"
B = "\x1b[0;94m"
BM = "\x1b[0;96m"

class Main(object):
	
	def __init__(self,url,token):
		self.url = url
		self.token = token
	def cek_account(self,id):
		try:
			__cek = json.loads(req.get(f"{self.url}/{id}?access_token={self.token}").text)
			nama = __cek['name']
			return nama
		except KeyError:
			return False

class Dump(Main):
	
	def pertemanan(self,id):
		global hitung
		if self.cek_account(id) == False:
			exit(f"[{BM}!{P}] {M}Ops.. Target tidak ditemukan.{P}")
		else:
			print(f"[{BM}={P}] Nama target: {self.cek_account(id)}")
		try:
			__r=json.loads(req.get(f"{self.url}/{id}/friends?limit=5000&access_token={self.token}").text)
			for __data in __r['data']:
				nama = __data['name'].rsplit(" ")[0]
				id = __data['id']
				tampung.append(nama + "<=>" + id)
		except Exception as e:
			try:
				print(f"\n{M} * {__r['error']['message']}{P}\n {K}* Tunggu 2 jam atau ganti tumbal jika ingin lebih cepat!{P}")
			except:
				print(f"Error: {M}{e}{P}")
		for b in range(len(tampung)):
			hitung+=1
			print(f"\r[!] Mengumpulkan {BM}{hitung}{P} ID	",end="")
			time.sleep(0.001)
		print("")
		time.sleep(2)
		print(f"\n[=] Total id -> {H}{len(tampung)}{P}")
		if (len(tampung))==0:
			exit(f"[{BM}!{P}] {M}Ops! Jumlah id hanya terdapat 0.{P}")
		else:
			return tampung
	
	def followers(self,id):
		global hitung
		if self.cek_account(id) == False:
			exit(f"[{BM}!{P}] {M}Ops.. Target tidak ditemukan.{P}")
		else:
			print(f"[{BM}={P}] Nama target: {self.cek_account(id)}")
		try:
			__r=json.loads(req.get(f"{self.url}/{id}/subscribers?limit=5000&access_token={self.token}").text)
			for __data in __r['data']:
				nama = __data['name'].rsplit(" ")[0]
				id = __data['id']
				tampung.append(nama + "<=>" + id)
		except Exception as e:
			try:
				print(f"\n{M} * {__r['error']['message']}{P}\n {K}* Tunggu 2 jam atau ganti tumbal jika ingin lebih cepat!{P}")
			except:
				print(f"Error: {M}{e}{P}")
		for b in range(len(tampung)):
			hitung+=1
			print(f"\r[!] Mengumpulkan {BM}{hitung}{P} ID	",end="")
			time.sleep(0.001)
		print("")
		time.sleep(2)
		print(f"\n[=] Total id -> {H}{len(tampung)}{P}")
		if (len(tampung))==0:
			exit(f"[{BM}!{P}] {M}Ops! Jumlah id hanya terdapat 0.{P}")
		else:
			return tampung
	
