import requests

def search(keyword):
    url = 'https://www.so.com/s'
    params = {
        'q': keyword
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
    }
    resp = requests.get(url, params=params, headers=headers)
    return resp.text, resp.url


if __name__ == '__main__':
    keyword = input('input keyword:')
    text, url = search(keyword)
    print('text:', text)
    print('url:', url)
