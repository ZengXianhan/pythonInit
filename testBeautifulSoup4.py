import urllib.request
from bs4 import BeautifulSoup

url = "https://zh.wikipedia.org/wiki"

request2 = urllib.request.Request(url)
request2.add_header("user-agent","Mozilla/5.0")
response2 = urllib.request.urlopen(request2)
html_doc = response2.read()

soup = BeautifulSoup(html_doc, 'html.parser',from_encoding='utf-8')
print("Get all link")
links = soup.find_all('a')
for link in links:
    try:
        print(link.name, link['href'], link.get_text())
    except:
        continue

print("Get one head")
head_node = soup.find('h1',class_='firstHeading')
print(head_node.name, head_node.get_text())
