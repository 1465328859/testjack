import urllib.request
from unittest import runner

import requests
import unittest
class login (unittest.TestCase):
    def setUp(self) -> None:
        self.host='http://admin01.mycpw99.com/api'
        self.headers ={'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Access-Token': '',
        'channel': '',
        'Connection': 'keep-alive',
        'Host': 'admin01.mycpw99.com',
        'Referer': 'http://admin01.mycpw99.com/user/login?redirect=%2F',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    def test_public(self):
        url=self.host + '/admin/public'
        request = requests.get(url).json()
        if request['result'] == 200000:
            print('/admin/public接口没问题')
            print('返回渠道：' + request['data']['channel'])

    def test_login(self):
        url=self.host+'/admin/login'
        request=requests.post(url,json={"username":"jack000","password":"jack000","channel":"LY"}).json()
        if request['result'] ==200000 and request['data']['username'] == "jack000":
            print('/admin/login接口没问题')
            file=open('admintoken',"w+")
            file.write(request['data']['token'])
            file.close()
        else:
            print('/admin/login接口有问题')
            print('返回状态码：'+str(request['result']))

    def test_categorygameslist(self):
        url=self.host+'/games/categorygameslist'
        token = open('admintoken','r')
        gettoken=token.read()
        token.close()
        self.headers['Access-Token']=gettoken
        request=requests.get(url,headers=self.headers).json()
        print(request)
        if request['result'] == 200000:
            print('/games/categorygameslist接口没问题')
        else:
            print('/games/categorygameslist接口有问题')
            print('返回状态码：' + str(request['result']))
            print('msg'+request['msg'])
            print(request)


    def tearDown(self) -> None:
        print('运行完毕')
if __name__=='__main__':
    runner.run()