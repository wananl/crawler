import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html


def get_page(url):
    html = url_open(url).decode('utf-8')


    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    print(html[a:b])
    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('a href=')

    while a != -1:
        b = html.find('.', a, a+255)
        if b != -1:
            img_addrs.append('http:'+html[a+8:b+30])
        else:
            b = a + 9

        a = html.find('a href=', b)


    for i in img_addrs:
        print(i)


def save_imgs(folder, img_addrs):

    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_mm(folder='OOXX', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)



if __name__ == '__main__':
    download_mm()