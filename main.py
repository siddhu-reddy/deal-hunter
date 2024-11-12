import requests
from bs4 import BeautifulSoup

url = "https://dealsheaven.in/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
deal_cards = soup.find_all('div', class_='deatls-inner') 
for deal_card in deal_cards:
    title = deal_card.find('h3').text.strip()
    price = deal_card.find('p', class_='price').text.strip()
    special_price = deal_card.find('p', class_='spacail-price').text.strip()
    print(f"Title: {title}")
    print(f"Original Price: {price}")
    print(f"Special Price: {special_price}")
    print()

