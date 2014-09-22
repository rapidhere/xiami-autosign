# -*- coding: utf8 -*-

import requests
import simplejson

email = r""
password = r""

login_url = r"https://login.xiami.com/member/login"
signin_url = r"http://www.xiami.com/task/signin"
cookie_url = r"http://www.xiami.com/index/home"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36",
    "Pragma": "no-cache",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    "Accept-Encoding": "gzip,deflate,sdch",
}

# create session
sess = requests.Session()

def login():
    # login
    login_data = {
        "done": "http://www.xiami.com",
        "from": "web",
        "email": email,
        "password": password,
        "submit": "登 录",
    }

    r = sess.post(login_url, headers=headers, data=login_data)
    rjson = simplejson.loads(r.content)

    if not rjson["status"]:
        raise Exception("Login failed!")

def signin():
    # complete sessions
    r = sess.get(cookie_url, headers=headers)

    # sign in
    r = sess.post(signin_url, data={}, headers={
        "Referer": "http://www.xiami.com/member/login",
        "User-Agent": 'Mozilla/5.0 (IsomByt; checker)',
    })

    # get result
    r = sess.get(cookie_url, headers=headers)
    rjson = simplejson.loads(r.content)

def mail_out(message):
    pass

if __name__ == "__main__":
    try:
        login()
        signin()
    except Exception as e:
        mail_out(str(e))

