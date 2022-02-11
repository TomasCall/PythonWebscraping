import requests
from bs4 import BeautifulSoup


interests = ["orosz","covid","koronavírus","covid-19","péter","mzp","ellenzék","vírus","fertőzött"]


def scraper(url,file):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.select('a')
    lst = []
    for item in links:
        tmp = item.text.strip().lower()
        for interest in interests:
            if interest in tmp and tmp not in lst:
                if "hvg" in url:
                    print(f'<a href="{url}{item.get("href")}">{item.text.strip()}</a>',file=file)
                    lst.append(tmp)
                else:
                    if "slug" not in item.get("href"):
                        print(f'<a href="{item.get("href")}">{item.text.strip()}</a>',file=file)
                        lst.append(tmp)


def main():
    file = open("cikkek.html","w")
    print("<html lang='en'>",file=file)
    print("<head>",file=file)
    print("<link rel='stylesheet' type='text/css' href='styles.css'>",file=file)
    print("<meta charset='UTF-8'>",file=file)
    print("<title>Document</title>",file=file)
    print("</head>",file=file)
    print("<body>",file=file)
    print("<div class='wrapper'>",file=file)
    
    print("HVG.hu adatok átnézése")
    
    print("<h1>HVG</h1>",file=file)
    scraper("https://hvg.hu",file)
    print("<h1>444</h1>",file=file)
    scraper("https://444.hu",file)

    print("444.hu adatok átnézése")
    
    print("</div>",file=file)
    print("</body>",file=file)
    print("</html>",file=file)

    print("Befejezve!")


if __name__ == "__main__":
    main()