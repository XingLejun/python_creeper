#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, values in r.cookies.items():
#     print(key + '=' + values)


# 正则匹配
import re
content ='Hello 1234567   8576485 World_This is a Regex Demo'
print(len(content))
print(content[24])
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}\s\w{2}\s\w\s\w{5}\s\w{4}', content)
# result = re.match('^Hello\s(\d+)\s{3}(\d+)\sWorld', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# print(result.span())

result = re.match('^Hello.*Demo$', content)
print(result.group())
