import requests
import http.cookiejar as cookielib
import re
import pickle

agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
header = {
    "host": "www.zhihu.com",
    "referer": "https://www.zhihu.com",
    "user-agent": agent
}

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename= "cookies.txt")

def get_xrsf():
    response = session.get("https://www.zhihu.com/", headers = header)
    print(response.text.encode("utf-8"))
    return ""

def get_index():
    response = session.get("https://www.zhihu.com/", headers = header)
    with open("index_page.html","wb") as f:
            f.write(response.text.encode("utf-8"))
    print("ok")

def zhihu_login(account, password):
    if re.match("^1\d{10}", account):
        print("mobile login")
        post_url = "https://www.zhihu.com/api/v3/oauth/sign_in"
        post_data = {
            "_xsrf": get_xrsf,
            "phone_num": account,
            "password": password
        }
        response_text=session.post(post_url, data=post_data, headers= header)
        session.cookies.save()
        print("login done")

zhihu_login("15008449923","zxh19933813")
get_index()