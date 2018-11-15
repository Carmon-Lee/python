import http.cookiejar
import urllib.request
import re

def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

header={'Content-Type': "application/x-www-form-urlencoded"}
url = 'http://www.zdic.net/sousuo/'

opener = getOpener(header)
# op = opener.open(url)
# resp = op.read().decode('utf-8')
# print(resp)
#
# url += 'login'
# id = '这里填你的知乎帐号'
# password = '这里填你的知乎密码'

postDict = {
    'lb_a':'hp',
    'lb_b':'mh',
    'lb_c':'mh',
    'tp':'tp1',
    'q':'好'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
resp = op.read().decode('utf-8')
resp=re.sub('\n','',resp)
# print(resp)


rule= '<p class="zdct5">.*?</p>'
pat=re.compile(rule)
details=re.findall(pat,resp)

pinyin=re.findall(re.compile('/z/pyjs.*?</a>'),resp)
for i in details:
    print(i)

#
# print(data.decode())  # 你可以根据你的喜欢来处理抓取回来的数据了!