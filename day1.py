import requests

par= {"wd": "python"}
r = requests.get("https://www.baidu.com/s", params=par)

# print(r.status_code)
# print(r.text)

help(requests)


