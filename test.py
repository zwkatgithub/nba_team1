from bs4 import BeautifulSoup

html = '<div> hello</div> <!--<div>sonp</div>-->'
soup = BeautifulSoup(html,'lxml')
divs = soup.find_all('div')
for div in divs:
    print(div.text)