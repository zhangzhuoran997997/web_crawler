from urllib.request import urlopen

url = "http://www.baidu.com"
response = urlopen(url)

print(response.read().decode("UTF-8"))