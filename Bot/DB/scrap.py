from bs4 import BeautifulSoup
import requests
from fake_headers import Headers
import lxml

domain_name = 'https://www.google.com/finance/quote/USD-UAH'
headers = Headers(headers=True).generate()
    
class Scraper:
    def __init__(self, url=domain_name):
        self.url = url
        self.soup: BeautifulSoup
    
    @staticmethod
    def response(url: str) -> requests.Response:
        try:
            result = requests.get(url, headers=headers)
            print(f'{result}\nResponse received')
            return result
        except:
            print(f'No Response')
    
    def search_price(self):
        scr = self.response(self.url)
        if scr:
            self.soup = BeautifulSoup(scr.text, 'lxml')
        else:
            raise AttributeError
        price = self.soup.find('div', class_='YMlKec fxKbKc')
        print(price.text)
        return price.text

if __name__ == "__main__":
    scraper = Scraper()
    scraper.search_price()