import urllib.request
import http.cookiejar as cookiejar

url = "http://www.google.com"

print("Test 1")
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print("Test 2")
request2 = urllib.request.Request(url)
request2.add_header("user-agent","Mozilla/5.0")
response2 = urllib.request.urlopen(request2)
html = response2.read()
print(response2.getcode())
print(len(response2.read()))

print(html.decode('utf-8'))