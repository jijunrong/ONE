import requests
import random

# 目标网站列表
urls = [
    'https://blog.jijunrong.com',
    'https://blog.jijunrong.top',
    'https://blog.jijunrong.site',
    'https://one.jijunrong.com',
    'https://one.jijunrong.top',
    'https://one.jijunrong.site',
    'https://one.jijunrong.one'
]

# 访问网站函数
def visit_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"成功访问 {url}.")
        else:
            print(f"访问 {url} 失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"访问 {url} 时发生错误: {e}")


# 遍历网站列表，每个网站访问一次
for url in urls:
    visit_site(url)
    time.sleep(random.uniform(1, 5))  # 随机等待1到5秒
