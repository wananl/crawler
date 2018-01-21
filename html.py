import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html





def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src=', b)


    return img_addrs


def save_imgs(folder, img_addrs):


    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)



def download_mm(folder='OOXX'):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://www.jder.net/meizi/108324.html'





    img_addrs = find_imgs('http://www.jder.net/meizi/108324.html')
    save_imgs(folder, img_addrs)



if __name__ == '__main__':
    download_mm()