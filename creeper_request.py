#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.text)
# print(type(r.text))

import re
headers= {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)'
}
r = requests.get('https://book.douban.com/', headers=headers)
pattern = re.compile('<p class="abstract">.*? </p>', re.S)
titles = re.findall(pattern,r.text)
print(titles[15])
print(type(titles))

# GigHub图标
# r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# with open('favicon.ico', 'wb') as f:
#    f.write(r.content)