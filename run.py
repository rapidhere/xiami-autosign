# -*- coding: utf8 -*-

import requests
import simplejson

email = r""
password = r""

login_url = r"https://login.xiami.com/member/login"
signin_url = r"http://www.xiami.com/task/signin"

headers = {
    "Host": "www.xiami.com",
    "Referer": "http://www.xiami.com/",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36",
    "Pragma": "no-cache",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    "Accept-Encoding": "gzip,deflate,sdch",
}

# create session
sess = requests.Session()

# login
login_data = {
    "done": "http://www.xiami.com",
    "from": "web",
    "email": email,
    "password": password,
    "submit": "登 录",
}

r = sess.get("http://www.xiami.com/index/home", headers=headers)

# sign in
r = sess.post(signin_url, data={}, headers={
    "Referer": "http://www.xiami.com/member/login",
    "User-Agent": 'Mozilla/5.0 (IsomByt; checker)',
})
