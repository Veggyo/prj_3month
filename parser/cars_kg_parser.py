import requests
from bs4 import BeautifulSoup as BS

URL = 'https://cars.kg/offers'
page = 0

while True:
    page += 1
    url = URL + f'{page}'
    response = requests.get(url=URL, timeout=10)
    if response.status_code == 200:
        end = 'По заданным критериям не найдено ни одного предложения'
        break
    soup = BS(response.text, 'html.parser')
    cars_list = soup.find('div', class_='catalog-list')

    for c in cars_list.find_all('a', class_='catalog-list-item'):
        model = c.find('span', class_='catalog-item-caption')
        params = c.find('span', class_='catalog-item-params')
        more = c.find('span', class_='catalog-item-descr')
        info = c.find('span', class_='catalog-item-info')
        views = c.find('span', class_='catalog-item-views')
        year = model.find(class_='caption-year').text
        model = model.text.replace(f" , {year}", '').strip()
        print(model)
