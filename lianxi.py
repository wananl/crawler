import urllib.request
import re
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()



    return html

def find_img(url):
    p = r'<img src="([^"]+\.jpg)"'
    imglist = re.findall(p, url_open(url).decode('utf-8'))


    return imglist

def save_img(imglist):
    for each in imglist:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder='girl'):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://www.jder.net/meizi/108246.html'

    imglist = find_img(url)
    save_img(imglist)



if __name__ == '__main__':
    download_mm()