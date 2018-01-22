import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_img(html):
    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    imglist = re.findall(p, html)

    for each in imglist:
        print(each)

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/'
    get_img(open_url(url))