import requests
from bs4 import BeautifulSoup
import json

def parse_ai():
    url = "https://abit.itmo.ru/program/master/ai"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # пример простого парсинга названий элективов
    electives = []
    for li in soup.find_all('li'):
        if "электив" in li.text.lower():
            electives.append(li.text.strip())
    # можно расширить, если на сайте таблица или список в другом месте
    with open('plans/ai.json', 'w', encoding='utf-8') as f:
        json.dump({"electives": electives}, f, ensure_ascii=False, indent=2)

def parse_ai_product():
    url = "https://abit.itmo.ru/program/master/ai_product"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    electives = []
    for li in soup.find_all('li'):
        if "электив" in li.text.lower():
            electives.append(li.text.strip())
    with open('plans/ai_product.json', 'w', encoding='utf-8') as f:
        json.dump({"electives": electives}, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    parse_ai()
    parse_ai_product()
    print("Учебные планы обновлены!")
