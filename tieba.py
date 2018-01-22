import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_img(html):
    p = r'<img src="([^"]+\.jpg)"'
    imglist = re.findall(p, html)

    for each in imglist:
        print(each)
    '''
    for each in imglist:
        filename = each.split('/')[-1]
        urllib.request.urlretrieve(each, filename, None)
    '''
if __name__ == '__main__':
    url = 'http://www.jder.net/meizi/108246.html'
    get_img(open_url(url))