import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
}

# 主页上每篇文章的标题、阅读数、点赞数和收藏数
def get_article_info(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    try:
        blog_title = soup.find(class_='titName SG_txta').text
        uid = url[-21:-13]
        aid = url[-11:-5]
        resp = requests.get('http://comet.blog.sina.com.cn/api?maintype=num&uid=' + uid + '&aids=' + aid)
        f = re.search(r'"f":(\d+)', resp.text).group(1) #收藏
        d = re.search(r'"d":(\d+)', resp.text).group(1) #喜欢
        r = re.search(r'"r":(\d+)', resp.text).group(1) #阅读
        return blog_title, f, d, r
    except AttributeError:
        return get_article_info(url)
    
# 主页标题、博客访问量、全部博文数目
def get_blog_info(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    home_title = soup.title.text.split('_')[0] + '的博客'
    visits = soup.find(id='comp_901_pv').text
    blogs = soup.find(class_='SG_page')['total']
    print(f'主页标题:{home_title}\n博客访问量:{visits}\n全部博文数目:{blogs}\n')

    bloglist = soup.find(class_='bloglist')
    for blog_title in bloglist.find_all(class_='blog_title'):
        blog_url = blog_title.a['href']
        blog_title, f, d, r = get_article_info(blog_url)
        print(f'标题:{blog_title}')
        print(f'阅读数:{r} 点赞数:{d} 收藏数:{f}\n')

if __name__ == '__main__':
    get_blog_info('http://blog.sina.com.cn/weiyouzhonghua')
