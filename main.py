from crypto_scraper import CryptoCurrency
import time
import os

if __name__ == '__main__':
    while True:
        symbol1 = CryptoCurrency(symbol='btcusd')
        symbol2= CryptoCurrency(symbol='ethusd')
        CryptoCurrency.show_prices()
        time.sleep(3)
        CryptoCurrency.clean_prices()
        os.system("cls")
        