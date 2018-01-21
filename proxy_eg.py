import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

iplist = ['113.206.180.252:8118', '111.132.193.159:8118', '223.241.119.244:8010']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)