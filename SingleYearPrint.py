from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time

yr = 2021

url = "https://www.sports-reference.com/cbb/postseason/men/" + str(yr) + "-ncaa.html"
try:
    html = urlopen(url)
except HTTPError as err:
    secs = int(err.headers["Retry-After"])
    print("wait " + str(secs/60) + " minutes...")
    time.sleep(secs)
    html = urlopen(url)

html = html.read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)