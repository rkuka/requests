import requests
from lxml import etree
import time

nbd ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

ck = requests.get('https://pmsearch.jd.com/?publishSource=7&childrenCateId=13812',nbd)
#ck = requests.get(
    #'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fprodev.jd.com%',nbd)

print(ck.text)

sj=etree.HTML(ck.text)

time.sleep(30)