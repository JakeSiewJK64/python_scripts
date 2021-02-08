from bs4 import BeautifulSoup
from urllib.request import urlopen

# 1. opens the url
# 2. reads the HTML fron the apge as a string and assigns it to html variable
# 3. creates a beautifulsoup object
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
soup_text = soup.get_text()

soup.find_all("img")
print(browser.get(url))


