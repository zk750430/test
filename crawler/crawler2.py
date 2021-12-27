import requests
import re
from bs4 import BeautifulSoup
import os

# 获取想要爬取的小说url
urls = ["http://reader.epubee.com/books/mobile/89/899b8265ceaf9d149b6fa532f953b7e9/text00000.html"]
url_prefix = "http://reader.epubee.com"


def get_url_suffix(url_all):
    r = requests.get(url_all, verify=False)
    r.encoding = "utf-8"
    selector = BeautifulSoup(r.text, 'html.parser')
    for url_suffix in selector.find("div", class_="menu-inner scroll-bar").find_all("a", href=re.compile("/books/mobile")):
        get_text(url_prefix,url_suffix.get("href"))

def get_text(url_prefix,url_suffix):
    url = url_prefix+url_suffix
    number =url_suffix[-8:-5]
    r = requests.get(url, verify=False)
    r.encoding = "utf-8"
    selector = BeautifulSoup(r.text, 'html.parser')
    # # 获取文章标题
    title = selector.find("a", href=url_suffix).text
    # # 获取小说内容
    text = selector.find("div",class_="readercontent-inner").text
    # # 解决文件名带有转义字符导致在Windows系统下出现问题
    intab = "?*/\|.:><"
    outab = "         "
    trantab = str.maketrans(intab, outab)
    title = title.translate(trantab)
    # 设置保存小说的路径
    path = r"D:\毛选\ "
    if number >= "000" and number<"019":
        with open(path+"第一卷\\" + title, 'w', encoding="utf-8") as f:
            for i in text:
                f.write(i)
    elif number>="019" and number <"060":
        with open(path+"第二卷\\" + title, 'w', encoding="utf-8") as f:
            for i in text:
                f.write(i)
    elif number>="060" and number <"092":
        with open(path+"第三卷\\" + title, 'w', encoding="utf-8") as f:
            for i in text:
                f.write(i)
    elif number>="092" and number <"163":
        with open(path+"第四卷\\" + title, 'w', encoding="utf-8") as f:
            for i in text:
                f.write(i)
    else:
        with open(path +"第五卷\\" + title, 'w', encoding="utf-8") as f:
            for i in text:
                f.write(i)




if __name__ == "__main__":
    for url_all in urls:
        get_url_suffix(url_all)


