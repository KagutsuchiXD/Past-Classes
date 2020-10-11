from urllib.parse import urlparse
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

urlSet = set()

o = urlparse('https://www.usu.edu/')
r = requests.get(o.geturl())
soup = BeautifulSoup(r.text, "lxml")
newlink = ''

for link in soup.find_all('a'):
    nextlink = urlparse(link.get('href'))
    if nextlink.scheme != 'http' and nextlink.scheme != 'https':
        newlink = urljoin(o.geturl(), nextlink.geturl())
    else:
        newlink = nextlink.geturl()
    if newlink in urlSet:
        pass
    else:
        urlSet.add(newlink)
        print(newlink)

# print(o.geturl())
# print(o)
# print(r.text)
