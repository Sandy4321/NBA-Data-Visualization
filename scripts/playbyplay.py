from bs4 import BeautifulSoup

soup = BeautifulSoup(open("playbyplay.html"), "html.parser")

tables = soup.findAll("tr")

for table in tables:
  if table.findParent("tr") is None:
    print str(table)