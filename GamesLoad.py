from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time

f = open("gameLog.txt", "a")
year1 = 2021
year2 = 2024

for yr in range(year1, year2+1, 1):
    print(yr)
    f.write(str(yr) + '\n')
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

    text = text.split('\n')
    ii = 0
    while text[ii] != 'National':
        ii += 1
    ii += 1

    # seed school score seed school score location
    for y in range (4):
        while text[ii] != '1':
            ii += 1
        for x in range(15):
            f.write(text[ii] + " " + text[ii+1] + " " + text[ii+2] + "-" + text[ii+5] + " " + text[ii+3] + " " + text[ii+4] + "\n")
            ii += 6
            while len(text[ii]) > 2:
                ii += 1
        ii += 2

    for z in range(3):
        f.write(text[ii] + " " + text[ii+1] + " " + text[ii+2] + "-" + text[ii+5] + " " + text[ii+3] + " " + text[ii+4] + "\n")
        ii += 6
        while len(text[ii]) > 2:
            ii += 1

f.close()