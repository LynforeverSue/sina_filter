# encoding=utf-8
import json
import base64
import requests


myWeiBo = [
    {'no': 'wwsd22@163.com', 'psw' : '2456we4'},
    {'no': 'nwjde40120@163.com', 'psw': '7d7xxzcp73'},
    {'no': 'jixingtangwm861@163.com', 'psw': '7x0fmmx68b'},
    {'no': 'vbiqinchi57774@163.com', 'psw': '1yeg9pvgao'},
    {'no': 'myqf08935952@163.com', 'psw': '4gu33bk12w'},
    {'no': 'lmiwemyueil5@163.com', 'psw': '7ll6cjryg0'},
    {'no': 'ohprdkav5213@163.com', 'psw': '4bzp6jlc55'},
    {'no': 'xdtdaa8675040@163.com', 'psw': '1ghqfo37yq'},
    {'no': 'uodr985400@163.com', 'psw': '7et2jcab8K'},
    {'no': 'dqvenx38455@163.com', 'psw': '7sc4kk35xu'},
    {'no': 'sfey968@163.com', 'psw': '0ng0ugtci'},
    # {'no': 'yiyongm1515@163.com', 'psw': 'wasd5614'},
    # {'no': 'nvnm350@163.com', 'psw': 'jerga456'},
    {'no': 'wvdz281@163.com', 'psw': 'hwt9035'},
    {'no': 'uwye78@163.com', 'psw': 'hytr41'},
    # {'no': 'dbgs876@163.com', 'psw': '878tyuv'},

    # {'no': 'wer3612@163.com', 'psw': '288uyx'},
    {'no': 'qpah34@163.com', 'psw': '2456we245'},
    {'no': 'qpzm543@163.com', 'psw': '2496we22'},
    # {'no': 'laki1222@163.com', 'psw': '256we22'},
    # {'no': 'sie987@163.com', 'psw': '2456we22'},
    {'no': 'sjdgdy12@163.com', 'psw': '123456we4'},
    {'no': 'yaya87652@163.com', 'psw': '123456qwe5'},

    {'no': 'rwiua48@163.com', 'psw': 'mcb3168'},
    {'no': 'bsen33@163.com', 'psw': 'htzse438165'},
    {'no': 'cjjm705@163.com', 'psw': 'hzq748'},
    {'no': 'eurh164@163.com', 'psw': 'ukze60989'},
    {'no': 'hbdt638@163.com', 'psw': 'pmng458	'},
    {'no': 'xlci728@163.com', 'psw': 'fzoehrizi714'},
    {'no': 'mocf119@163.com', 'psw': 'tta49649'},
    {'no': 'dksp93@163.com', 'psw': 'ztmmyu288'},
    {'no': 's29407@163.com', 'psw': 'erq708'},
    {'no': 't59692@163.com', 'psw': 'phrfo82794655'},



    # {'no': 'jiadieyuso3319@163.com', 'psw': 'a123456'},
    # {'no': 'shudieful3618@163.com', 'psw': 'a123456'},
]


def getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    for elem in weibo:
        account = elem['no']
        password = elem['psw']
        username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": username,
            "service": "sso",
            "sp": password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        session = requests.Session()
        r = session.post(loginURL, data=postData)
        jsonStr = r.content.decode('gbk')
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            print "Get Cookie Success!( Account:%s )" % account
            cookie = session.cookies.get_dict()
            cookies.append(cookie)
        else:
            print "Failed!( Reason:%s )" % info['reason']
    return cookies


cookies = getCookies(myWeiBo)
print "Get Cookies Finish!( Num:%d)" % len(cookies)
