import bs4
import requests
from bs4 import BeautifulSoup


# res = requests.get("https://item.jd.com/100008348542.html")
# print(res.status_code)
# print(res.text[:100])

# url = "http://m.ip138.com/ip.asp?ip="
# r = requests.get(url+'202.204.80.112')
# print(r.status_code)
# print(r.text)
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# print(soup.findAll("p"))

# res1 = requests.get("http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html")
# print(res1.status_code)


# 获取rl的HTML的text
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(uList, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            uList.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(uList, num):
    # tplt中第二个参数中的{3}表示在format函数中使用第三个参数进行缺省填充
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}\t"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = uList[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


if __name__ == "__main__":
    uInfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uInfo, html)
    printUnivList(uInfo, 20)
