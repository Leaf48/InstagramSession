import requests
import os
import fake_useragent

ua = fake_useragent.UserAgent()

se = requests.session()

login_url = 'https://www.instagram.com/accounts/login/ajax/'

login_headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "267",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "ig_did=0897491F-B736-4E7E-A657-37438D0967B8; csrftoken=xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe; rur=FTW; mid=XxTPfgALAAGHGReE-x_i1ISMG4Xr",
    "origin": "https://www.instagram.com",
    "referer": "https://www.instagram.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": F"Mozilla/91.81 (Linux; Android 6.3; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36",
    "x-csrftoken": "xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe",
    "x-ig-app-id": "1217981644879628",
    "x-ig-www-claim": "0",
    "x-instagram-ajax": "180c154d218a",
    "x-requested-with": "XMLHttpRequest"
}

username = ""
password = ""

login_data = {
    "username": username,
    "enc_password": "#PWD_INSTAGRAM_BROWSER:0:&:" + password
}

login = se.post(login_url, data=login_data, headers=login_headers)

print(login.json())




