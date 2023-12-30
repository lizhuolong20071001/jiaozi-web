import requests
import json
version = "12.0.0"
url = f"http://127.0.0.1:8000/api/?new_version={version}"
download_name = "1.txt"
r = requests.get(url)
print(r.json())
print(type(r.json()))
c = r.json()
if c == 0:
    print("请尽快更新，下载文件请扣1")
    a = input()
    a = int(a)
    if a == 1:
        url_file = f"http://127.0.0.1:8000/download/?download_name={download_name}"
        r = requests.get(url_file, stream=True)
        f = open("1.txt", "wb")
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)

