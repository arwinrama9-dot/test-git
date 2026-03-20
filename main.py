import requests

# 尝试访问一个网站
try:
    response = requests.get("https://www.google.com", timeout=5)
    print(f"成功！状态码: {response.status_code}")
except Exception as e:
    print(f"访问失败: {e}")