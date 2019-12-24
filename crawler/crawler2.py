import requests
from lxml import etree
from bs4 import BeautifulSoup

# 获取想要爬取的小说url
urls = ["https://www.dingdiann.com/ddk74774/{}.html".format(i) for i in range(3954857, 3954887)]
# 设置保存小说的路径
path = r"C:\crawler\dingdian\带着仓库到大明\ "


def get_text(url):
    r = requests.get(url, verify=False)
    r.encoding = "utf-8"
    selector = BeautifulSoup(r.text, 'html.parser')
    # 获取文章标题
    title = selector.find("div", class_="bookname").find("h1").text
    # 获取小说内容
    text = selector.find("div", id="content").text

    # 解决文件名带有转义字符导致在Windows系统下出现问题
    intab = "?*/\|.:><"
    outab = "         "
    trantab = str.maketrans(intab, outab)
    title = title.translate(trantab)
    print(title)
    with open(path + title, 'w', encoding="utf-8") as f:
        for i in text:
            f.write(i)


if __name__ == "__main__":
    for url in urls:
        get_text(url)
