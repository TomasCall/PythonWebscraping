import requests
from bs4 import BeautifulSoup

class Depression:
    def __init__(self,bank_account_balance):
        self.bank_account_balance = bank_account_balance

    def get_value_of_euro(self):
        page = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=HUF")
        soup = BeautifulSoup(page.content, 'html.parser')
        my_paragraphs = soup.select("p")
        return float(my_paragraphs[2].text.strip().split()[0])


    def huf_to_euro(self):
        value = self.get_value_of_euro()
        return self.bank_account_balance/value


    def get_price_disel(self):
        page = requests.get("https://www.globalpetrolprices.com/Hungary/diesel_prices/")
        soup = BeautifulSoup(page.content, 'html.parser')
        my_tds = soup.select("td")
        return float(my_tds[2].text.strip())


    def liters_of_disel(self):
        return self.bank_account_balance/self.get_price_disel()


    def price_of_mort_subite(self):
        page = requests.get("https://www.arukereso.hu/sor-c1060/mort-subite/0-25l-pal-p505000558/")
        soup = BeautifulSoup(page.content, 'html.parser')
        my_span = soup.select("span")
        my_span = set(my_span)
        for item in my_span:
            if "Ft" in item.text.strip():
                return int(item.text.strip().split()[0])


    def liters_of_mort_subite(self):
        return (self.bank_account_balance/self.price_of_mort_subite())/4



