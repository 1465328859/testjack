# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import urllib.request
from lxml import html

def report(url):
    proxy = requests.get("http://cn-proxy.com/")
    proxytext=html.fromstring(proxy.text)
    index = 1

    while (index):
        xpath='//*[@id="post-4"]/div/div[4]/table/tbody/tr['+str(index)+']/td/text()'
        proxytable=proxytext.xpath(xpath)
        index+=1
        if proxytable:
            ip=proxytable[0]+':'+proxytable[1]
            proxyip=urllib.request.proxyHandler({"http":"http://"+ip})
            opener=urllib.request.build_opener(proxyip)
            urllib.request.install_opener(opener)
            data = urllib.request.urlopen('http://www.baidu.com',timeout=0).read().decode('utf-8','ignore')
            try:
                if (len(data) > 5000):
                    print(ip + ':可用')
                else:
                    print(ip + ':无效')
            except:
                    print(ip + ':无效！！!')
            print(proxytable[0]+':'+proxytable[1]+"       "+proxytable[2])
        else:
            break
    '//*[@id="post-4"]/div/div[4]/table/tbody/tr[1]'
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    report('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
