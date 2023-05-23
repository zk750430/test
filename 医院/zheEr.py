import random

import requests
import time
import base64
import hashlib
import urllib.parse
import json
import pyDes

key = 'yaolbDcJqlV6rVJPVi2K+e+qGEN6afOK'

# message = 'XhLBBH4OqKduKzFe5Ue3LwvaHV8KjWZAfacBzoUbIk5xFVhjvUJx%2 BcnhlZsJNcYJKVmmCWAGmr5%2 F0bQ2y02byP5FjVR%2 Fpw1xgf4L1RmxBMv%2 F%2 FBWUFu2ik8u6DuDjfVf9QPKlzowiqEKvJKC6dZjTCoRvZfqYplacUG%2 FAdmabRWrcMD2ptr3grHrrLbs73Atmq46vZd0V%2 BBcpja47GSMI4Es5Vwxw2ckOfTFJjeI%2 Fx9O6APIWqQ3%2 Bc4TzLYnSAxkQyeGVmwk1xgkpWaYJYAaavl%2 FcCcWbJwmD7xzOvkZ48wzatBk%2 B8Gl7KjXUargwu5DBaaOBGQxiCvs4rtJHux5%2 FUug821WqIfjqTxOxAd2H4mg94SGBS1G6tWppGVdeV1ltKGLvKxSfV7g1aioB8l68k5tnsMpTFWOv8c7dfKDI47JxHmBbjsMcO%2 B52c7slr5xgWZsz3PShqJaEUSjMFpLpLhj1SSYbeLAr9CH2%2 BTqcZiplMcM0uvf75LfxMxxwaulHdhaKaCzebMr72jvqaExumuOnMSehv2qSX7FKIPATL1X3PDrnUI7Ps46ey4AsREGRdgVcyN4PwiT0adExkBkWnPCktktEl8AfVR2EJ0S4cB7%2 FB6uLtmxZOLOmXUIe56JM%2 Bsm7E13rweqJfPhxvX4Ro93wj7M1%2 FRqppT7zL6tLqZAW1sPb%2 F3pxzvKON9U3UgqsnV5gY9F%2 BIf78JyKmGmJ6K2GpX%2 FUe1cUrf9G0NstNm8i5dnxcDUnTBvHO3XygyOOymjByTc7IQYL1M8WjHQr%2 BYNZb6S2uG6TWPy3euFaGQgUGSx%2 FZbvCGN8yD5Du%2 F%2 BpRvyPxe%2 BihZ3Fr9zx6zP%2 Bx8Z9jKHzZLjXU4kPMKtnvvEt3FksaUXMSVnV3Xg1D30RjrXnF8Fp45M22Vy0xb25CyP23xNjFprpsODkRBkeMGN2BVH4UEPc2GySVs4XwolK8Cz5ee9oOVzUFdeokNtlYFlnsUxScVPpTW8KS2S0SXwB9AQYvvBh3WpEe39Y63yaPqcQLqMGhxjRGY3bahpxm0lLvHf7QRkbBUfSzQ9aI62opa9gJW4tDV%2 FPfP6TxyuINJj3SxnL10BtyOGnZMS%2 FGWAYOx92f%2 BEmqMuxcHBNu9ERmR4KeDtbQHGqm6rtZ83To3LAkhBJQk8mzk%2 BUFWdU489bVeNF0Ybl3d0EAK48Ggk10LFchlc4a3XV6lVLxeTyzeJNfpp78IuNOhiXzXoOTI%2 B5%2 Bj6Mm5I5h4J5RGy2DunuFG7UhFjC%2 F5fEml7JmKe9Ukb4l0rWS23yaagLPS5RIrIp76RgiLXBBkFPcd6Gr9bpa7p1lFgz5Shj3XSLoDJ12trH8%2 Buu6YxK42%2 F2YbGaabZATUCpvuCN0RFsnzag%2 FU59JXg%2 Fnor3YX%2 Fkh9NGauxV%2 Fl96LmIJdFdIVGp3QRCq1amwZgjdUx94EPTs4Q4JtMHgSV7EsKyXKE3Kz7VnVtXp4xvXfje9MJcmcUr1rWdTlZ7Qc4MfLaPrFBR2Tc2ULnd5Tk4W31lmpZW%2 FCktktEl8AfytaY29qSdjEQIRD2MUsILmuFnrfRKSLx7z9gQax4vsjsDX%2 BQDW3fEj6HLS2k9rAY4vVEpLD0yE19zAv4xfLdEmYmrikC9%2 BWfW4v9%2 F7w3cHue%2 BkYIi1wQZDGfzc6Ow0ZzUG%2 FAdmabRWrcMD2ptr3grHrrLbs73Atmq46vZd0V%2 BBcpja47GSMI4Es5Vwxw2ckOH%2 BxO04Dsmg6iEMQAm2F%2 FrDbsuNEdZtqFVNKNQKn6bAWmCJlOeZ%2 F7EimBoPSYHEXEHBUZjijXgel4dTo%2 B9OYBe1Zb7evOAS8L4eiulhQ1Z1w5rUDxg%2 B0u3PY1D4tRwZKJMuQggGznzQdtzbWQCqQ9to7Wb5AAun%2 Bh0K%2 FIBT2sxG1kmVdgrEl8Bk3O4Lzx7cWw70VOy9QVsRW8jEHTg8%2 BIdTooAjXVcrrOJRf0yu%2 FQ%2 B1QM%2 FytxMz0ax%2 FGOsdrnu9523oySRPSQjEyZu%2 FSUTjFKCuM8AIMq4EQMXgsHiUD%2 BA0glOSKoXGkZ88w%2 FC3%2 F69rKWE5Th%2 BzeqmvGzjEI1uqHs5BAjI%2 FUZURuC0eQRb61ZTW8gRFWrY7ff12eo9xxSbPPgzt1VLnASUy5dEUAHElEbQrmHWnGAYod7vq6rheixA4dInbSUcHtYxFEIMvpqkwlTVphl%2 BxqFYAKg7mCAfNRFa%2 Blau1Ha0mgGUbB33Ta%2 FkLlIwYq5lsa3O%2 BRHHrY2ER4nXMGGEckoTWl8qFOiUM%2 F31t90jRldG2be%2 BQL6oSQEcc8Ki3aFFY1JkbzTC%2 F2DogXsoAcokTX%2 BdxU1m5X1W5m1Pf38x%2 BjnvEnt%2 FrBJYft4SuC9ZKXf9kB4TbJTELxfdEoSJO5zfk%2 FrdNEmaPdAbkqHzxNMrD%2 BZu%2 Bd1D%2 FblJpLlj7PErMO5hz69G5RU%2 ByUDuDqkVLxRPAViOENXq33mopQ0mYF%2 FJWJzt1skZlMpXkUSZMdJpeyZinvVJG%2 BJdK1ktt8mYvNOQpEKFGoFTgY2baqNYg3GQic%2 BbZ9%2 BS2lYxx2FUixy%2 BA3PHZJooPkfALE5b9juZBmEmWLIPNOgZZYHxc5PeMz8pTgtoxsengdj7knvGX2Gqi4dvzH9vLCIOrhz3k%2 B20rIY6y%2 BJSjH1swMh9xbpKJMXGPZv6GnilObqtODwBc39q%2 BjFEBjHD1dzatxAQc4dXh2FIi5%2 BzVO%2 F9y9sWpVP1OUwbsSETPEz9%2 BTsV1%2 BY%2 FHWsTt3ogPrFmg%3 D%3 D'
# message = message.replace(" ","")
# message = urllib.parse.unquote(message)
# base64_message = base64.b64decode(message)
k = pyDes.triple_des(key.encode('latin-1')[:24], pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)


# d = k.decrypt(base64_message)
# print(json.loads(d))
# print(d)

def hex_md5(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


def reqDecode(content):
    message = content.replace(" ", "")
    message = urllib.parse.unquote(message)
    base64_message = base64.b64decode(message)
    d = k.decrypt(base64_message)
    return json.loads(d)


def make_random(length):
    str = '0123456789'
    ret = ''
    for i in range(length):
        ret += str[random.randint(0, len(str) - 1)]
    return ret


def req():
    # url地址通过抓包工具Charles获取
    url = 'https://api.gjwlyy.com/api/app'
    # url = 'https://wxsrv.scmc.com.cn/common/api?cmd=DoctorDetailApp&doctorid=4187&nowday=0&platform=m&clinname=%E5%84%BF%E4%BF%9D%E7%A7%91'
    # 设置headers，特别是User-Agent和Cookie

    data = {"channel": "10", "format": "JSON", "oper": "127.0.0.1", "spid": "1001", "version": "6.1.0",
            "random": "7553", "service": "nethos.book.doc.scheme.list", "bookDocId": "2998", "_host": "www.gjwlyy.com",
            "_pv": "%23%2Fbook%2Fdoc%2F2998%3FbookDocId%3D2998%26bookDocName%3D%25E6%259B%25B9%25E4%25B9%2590%26bookSort%3D%25E9%25A2%2584%25E7%25BA%25A6%25E6%258C%2582%25E5%258F%25B7%26bookHosId%3D8%26platHosId%3D095102%26hosName%3D%25E6%25B5%2599%25E5%25A4%25A7%25E4%25BA%258C%25E9%2599%25A2%25E6%25BB%25A8%25E6%25B1%259F%25E9%2599%25A2%25E5%258C%25BA",
            "_device": "其他", "_aid": "oCvjPsMxE6xN0TfiZQYIumW7izSzqxNo"}
    password = "aAr9MVS9j1"
    random = make_random(4)
    data['random'] = random
    password_md5 = hex_md5(password)
    data_json = json.dumps(data)
    signStr = password_md5 + data_json
    sign = hex_md5(signStr)
    print(sign)
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '582',
        'Content-Type': 'application/json',
        'Host': 'api.gjwlyy.com',
        'Origin': 'https://www.gjwlyy.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.gjwlyy.com/',
        'Sec-Ch-Ua': "'Google Chrome'; v = '113', 'Chromium'; v = '113', 'Not-A.Brand';v = '24'",
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "'Windows'",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'sign': sign,
    }
    print(url)
    res = requests.post(url, headers=headers, json=data, cert=False)
    decodeConent = reqDecode(res.text)
    print(decodeConent)


if __name__ == "__main__":
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    req()
