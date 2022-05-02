import requests
from bs4 import BeautifulSoup, Tag
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
}

# 获取所有年级页面地址
def get_all_url():
    url = 'https://www.shicimingju.com/cate'
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    cate_divs = soup.find_all(class_=re.compile('^cate_card_sub card.*'))
    for cate_div in cate_divs:
        url = cate_div.find('a').get('href')
        yield f'https://www.shicimingju.com{url}'

# 在每一首诗词的页面提取该诗词的作品赏析内容
def get_shici_shangxi(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'lxml')
    result  = ''
    try:
        for child in soup.find('div', class_='shangxi_content'):
            if isinstance(child, Tag):
                if child.name == 'a':
                    result += child.text
                elif child.name == 'br':
                    child = str(child)
                    if child in ['<br>', '</br>', '<br/>']:
                        result += '\n'
                        continue
                    content = re.split('<br>|<br/>|</br>', child)
                    content = [x.strip() for x in content]
                    result += '\n'.join(content)
            else:
                result += child.strip()
    except TypeError:
        print(url)
        return '\n'
    return result

# 访问每个学期的页面，提取每一首诗词的编号、朝代、诗人、标题和内容
def get_all_shici(filename):
    with open(filename, 'w+', encoding='utf-8') as f:
        for url in get_all_url():
            resp = requests.get(url, headers=headers)
            resp.encoding = resp.apparent_encoding
            soup = BeautifulSoup(resp.text, 'html.parser')
            shici_card = soup.find(class_='card shici_card')
            f.write(shici_card.find('h1').get_text() + '\n\n')
            for line_div in shici_card.find_all('div', class_='line'):
                shici_div = line_div.next_sibling.next_sibling
                list_num_info_div = shici_div.find(class_='list_num_info')
                rex = re.search('>(.*?)<.+?>(.*?)<', str(list_num_info_div), re.S)
                # 编号、朝代、诗人
                number = rex.group(1).strip()
                dynasty = rex.group(2).strip()
                author = list_num_info_div.find('a').get_text()

                shici_list_main_div = shici_div.find(class_='shici_list_main')
                # 标题、链接地址
                title = shici_list_main_div.h3.a.text
                shici_url = 'https://www.shicimingju.com' + shici_list_main_div.h3.a.get('href')

                shici_content_div = shici_list_main_div.find(class_='shici_content')
                shici_list = []
                for child in shici_content_div:
                    if isinstance(child, Tag):
                        continue
                    shici_list.append(child.strip())
                display_none = shici_content_div.find(attrs={'style':'display: none'})
                if display_none:
                    for child in display_none:
                        if isinstance(child, Tag):
                            continue
                        shici_list.append(child.strip())
                # 内容
                shici_list = [x for x in shici_list if x != '']
                # 赏析
                shici_shangxi = get_shici_shangxi(shici_url)
                f.write(f'{number} {dynasty} {author} {title}\n')
                f.write('\n'.join(shici_list) + '\n\n')
                f.write(f'赏析:\n{shici_shangxi}\n\n')

if __name__ == '__main__':
    get_all_shici('shici.txt')