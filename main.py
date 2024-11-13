import requests
from bs4 import BeautifulSoup
import csv
url = "https://dealsheaven.in/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
with open('deals.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Original Price', 'Special Price'])

    deal_cards = soup.find_all('div', class_='deatls-inner') 
    for deal_card in deal_cards:
        title = deal_card.find('h3').text.strip()
        price = deal_card.find('p', class_='price').text.strip()
        special_price = deal_card.find('p', class_='spacail-price').text.strip()
        
        writer.writerow([title, price, special_price])
print("Data saved to deals.csv")
