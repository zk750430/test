import requests
from bs4 import BeautifulSoup
import pprint
import json


def download_all_htmls():
    htmls = []
    for idx in range(4):
        url = f"http://www.crazyant.net/page/{idx + 1}"
        print("craw html:", url)
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception("error")
        htmls.append(r.text)
    return htmls


htmls = download_all_htmls()


def parse_single_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all("article")
    datas = []
    for article in articles:
        # 查找超链接
        title_node = (
            article.find("h2", class_="entry-title").find("a")
        )
        title = title_node.get_text()
        link = title_node["href"]

        # 查找标签列表
        tag_nodes = (
            article.find("footer", class_="entry-footer").find("span", class_="tags-links").find_all("a")
        )
        tags = [tag_node.get_text() for tag_node in tag_nodes]
        datas.append(
            {
                "title": title,
                "link": link,
                "tags": tags
            }
        )
        return datas


all_datas = []
for html in htmls:
    all_datas.extend((parse_single_html(html)))


print(all_datas)
print(len(all_datas))
