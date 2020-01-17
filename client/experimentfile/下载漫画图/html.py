# coding: utf-8
import urllib2     # 该模块用于打开页面地址
import urllib      # 用于下载图片(为什么需要同时引进urllib和urllib2,请参考：https://www.cnblogs.com/wly923/archive/2013/05/07/3057122.html)
import re          # 用于正则表达式
import urlparse    # 将src拼接成一个可以直接访问的图片地址
import os          # 用于指定文件的保存地址
from bs4 import BeautifulSoup   # 用于将文档转为固定编码文件，便于从网页抓取数据


class Downloader(object):
    def html_download(self, url):    # 页面源码下载
        if url is None:
            return
        response = urllib2.urlopen(url)
        if response.getcode() != 200:      # 判断页面是否访问成功
            return
        html_cont = response.read()
        self.html_parse(url, html_cont)

    def html_parse(self, url, html_cont):   # 源码解析，提取需要的数据
        img_urls = []
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        imgs = soup.find_all('img', src=re.compile("/image/2017index/(.*)"))  # 根据src得到所有的img标签
        for img in imgs:
            new_url = img['src']  # 获取所有的链接
            new_full_url = urlparse.urljoin(url, new_url)  # 让new_url按照page_url的格式拼接成一个完整的url
            img_urls.append(new_full_url)
        self.img_download(img_urls)

    def img_download(self, img_urls):    # 文件下载保存
        if img_urls is None or len(img_urls) == 0:
            print 'no img can download'
            return

        cur_path = os.path.abspath(os.curdir)   # 获取当前绝对路径
        goal_path = cur_path + '\\' + 'imgs'   # 想将文件保存的路径
        if not os.path.exists(goal_path):      # os.path.isfile('test.txt') 判断文件夹/文件是否存在
            os.mkdir(goal_path)      # 创建文件夹
        count = 1    # 用于给图片命名
        for img in img_urls:
            print img
            urllib.urlretrieve(img, goal_path+'/'+str(count) + '.jpg')      # 下载图片，并进行命名（刚开始写这句的时候老是报错，后来才发现没有用str()进行类型转换，因为习惯了js的自动转换的思想，哈哈）
            count = count+1


if __name__ == '__main__':     # 程序运行入口
    root_url = 'http://www.quanjing.com/'   # 页面地址
    downloader = Downloader()
    downloader.html_download(root_url)