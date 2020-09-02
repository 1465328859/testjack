# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
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
            print(proxytable)
        else:
            break
    '//*[@id="post-4"]/div/div[4]/table/tbody/tr[1]'
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    report('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
