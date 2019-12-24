import requests
from bs4 import BeautifulSoup
import re

url = "https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all" \
      "&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1" \
      "&ie=utf8&initiative_id=tbindexz_20170306"

def getHTMLText(url):
    try:
        headers = {
            'cookie': 'thw=cn; cna=j7eEFTbInHYCAX122A0dth9j;'
                      ' t=11058fb03f2abb5b06f42551aa6344bd; miid=398580481910368187; '
                      'tracknick=%5Cu75DB%5Cu5374%5Cu4E0D%5Cu54ED; lgc=%5Cu75DB%5Cu5374%5Cu4E0D%5Cu54ED; '
                      'tg=0; enc=8HXwnf1TcWsqMqs%2Bp5yt08Qbq%2F1kiRywshcgXlKdzOLrYo32o63TomsFGp2hTmwN2EUnqZWNBlFICP5ch6d2Sg%3D%3D;'
                      ' hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__'
                      'll%3D-1%26_ato%3D0; UM_distinctid=16ca86bcc986db-069de76b3de726-7373e61-13c680-16ca86bcc9968f;'
                      ' mt=ci=3_1; _tb_token_=tT6BNcvCF28jclEEwtMG; cookie2=17d75ad23c4aae0a55f9c42e76f9813d;'
                      ' dnk=%5Cu75DB%5Cu5374%5Cu4E0D%5Cu54ED; _cc_=VT5L2FSpdA%3D%3D; v=0; '
                      'tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hmBhH%2BwrxntyHMW%2BAcTJnkCtaT'
                      'dvgFsMzxKv8jubBCR0u3JVqUkvNXA%2BDiJ298ARIEWb6nACgJrHOLZA%2F1HVqR9VsC4AnxMl%2'
                      'BblrsvyILzNx7oDpQCXu%2FOMAtMKX51ub%2B2vtpUdUw7K3a74El99lCJRVSg%2F1cMPRgChj'
                      'KVFohB7KsLMDF7CBzY7sqRJ6bICH%2F3NwY8EtRNPXFfJAIVlEDI8nxHGY15nntSD9owfY6hX0l'
                      'WWhFWraORDII%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com;'
                      ' _m_h5_tk=4c529055b979b984e210de4fbdb4e676_1577183465840; '
                      '_m_h5_tk_enc=57b416834981ab94ee2cdb7f95319d12; unb=1048864328; '
                      'uc3=nk2=rtGS6INpEQg%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dByuqh43bmFnq'
                      '9l%2Fw%3D&id2=UoH7I2HumlQFlg%3D%3D; csg=061cfae8; cookie17=UoH7I2HumlQFlg%'
                      '3D%3D; skt=8897c30f238ca0e0; existShop=MTU3NzE3NzQ3Ng%3D%3D; uc4=id4=0%40UOn'
                      'kRzotqBOQllt9NC%2FE8F6NXcfE&nk4=0%40rIs1J%2BrUtElYUTJcIYwGfaKqyw%3D%3D; _'
                      'l_g_=Ug%3D%3D; sg=%E5%93%AD82; _nk_=%5Cu75DB%5Cu5374%5Cu4E0D%5Cu54ED; '
                      'cookie1=AC0hYoD3sJwI3419JWUREpZcqQOLqnki8R%2FZ%2BFrd1II%3D; uc1=cookie16=V32'
                      'FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&cookie15='
                      'V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTbmhFpJDJjhg%3D%3D&'
                      'tag=8&lng=zh_CN; JSESSIONID=993F7537C49A88DE71BB5C2F89F7F5FE; l=cBIZ4a3Pvq'
                      'sS0GKDBOCZourza77T-IRfguPzaNbMi_5aE6YV3d_Ooj9xBFv6cjWhtmYB4WtSLwv9-At8JClXfo'
                      '_W4AadZ; isg=BHp6k46I8PRxin5kfWwKYItay6Bcg_92QAePNYRza43PdxuxbLtOFCSNw0MOZ3ad'
        }
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for j in range(len(plt)):
            price = eval(plt[j].split(":")[1])
            title = eval(tlt[j].split(":")[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


if __name__ == "__main__":
    goods = '书包'
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44 * i)
            html = getHTMLText(url)
            html_new = html.replace(r'<!--', '"').replace(r'-->', '"')
            parsePage(infoList, html_new)
        except:
            continue
    printGoodsList(infoList)
