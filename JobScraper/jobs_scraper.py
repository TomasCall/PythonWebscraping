import requests
from bs4 import BeautifulSoup


def schonerz_scraper():
    file = open("schonherz.html","w")
    print("Creating schonerz file")

    print('<!DOCTYPE html>',file=file)
    print('<html lang="en">',file=file)
    print('<head>',file=file)
    print('<meta charset="UTF-8">',file=file)
    print('<link rel="stylesheet" href="./jobs.css" type="text/css">',file=file)
    print('<title>Jobs</title>',file=file)
    print('</head>',file=file)
    print('<body>',file=file)
    print('<div class="wrapper">',file=file)
    print('<h1>Schönherz</h1>',file=file)
    print('<ul>',file=file)

    print("Scraping data")
    page = requests.get("https://schonherz.hu/diakmunkak/debrecen/fejleszto---tesztelo","html.parser")    
    soup = BeautifulSoup(page.content, 'html.parser')
    my_h4s = soup.select("h4")

    print("Writing data into html file")
    for item in my_h4s:
        tmp=str(item).split('"')[1]
        print(f'<li><a href="https://schonherz.hu/{tmp}">{item.text.strip()}</a></li>',file=file)

    print("Finishing file")

    print('</ul>',file=file)
    print('</div>',file=file)
    print('</body>',file=file)
    print('</html>',file=file)