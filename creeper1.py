import urllib.request
import urllib.parse

# 直接将结果写入文件
# response =urllib.request.urlretrieve('https://www.python.org', filename=r'/home/xinglejun/python_creeper/creeper1.html')
# 清除缓存
# urllib.request.urlcleanup()
# response =urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
# response =urllib.request.urlretrieve('https://www.baidu.com', data=data, filename= r'/home/xinglejun/python_creeper/ll.html')
# urllib.request.urlcleanup()
# print(response.readline())

# 添加请求体
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
