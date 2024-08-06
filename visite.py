import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# 定义网站列表
websites = [
    "https://blog.jijunrong.com",
    "https://blog.jijunrong.top",
    "https://blog.jijunrong.site"
]

# 获取本地IP地址和位置信息
def get_local_ip_and_location():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        ip = data.get("ip")
        location = data.get("city") + ", " + data.get("region") + ", " + data.get("country")
        return ip, location
    except Exception as e:
        print(f"无法获取本地IP地址和位置信息: {e}")
        return None, None

# 模拟不同设备的用户代理
user_agents = [
    # PC
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    # Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    # iPhone
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15A372 Safari/604.1",
    # 安卓
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"
]

# 创建浏览器会话
def create_browser(user_agent):
    options = Options()
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--headless")  # 无头模式，隐藏浏览器界面
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# 访问网站并执行操作
def visit_website(driver, url):
    try:
        driver.get(url)
        print(f"成功访问 {url}")
        # 停留至少10秒
        time.sleep(10)
        # 执行一些简单的操作
        actions = ActionChains(driver)
        actions.move_by_offset(10, 10).perform()  # 移动鼠标
        time.sleep(2)
        actions.click().perform()  # 点击
        print(f"在 {url} 上成功执行操作")
    except Exception as e:
        print(f"访问 {url} 时出错: {e}")

# 主函数
def main():
    ip, location = get_local_ip_and_location()
    print(f"本地IP地址: {ip}")
    print(f"位置信息: {location}")

    # 随机选择用户代理
    user_agent = random.choice(user_agents)
    print(f"使用的用户代理: {user_agent}")

    driver = create_browser(user_agent)

    for website in websites:
        visit_website(driver, website)

    driver.quit()

if __name__ == "__main__":
    main()
