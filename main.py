import requests
from bs4 import BeautifulSoup
from pathlib import Path

home_file = Path('home.txt')
def extract_links(base_url, url, checked_url_set):
    global home_file, url_file
    response = requests.get(url)
    if url == base_url:
        home_file.write_bytes(response.text.encode('utf-8'))

    data = BeautifulSoup(response.text, "html.parser")
    links = data.find_all('a')

    for link in links:
        href = link.get('href')
        address = None
        if href and href.startswith('/'):
            address = base_url + href
        elif href and href.startswith(base_url):
            address = href
        if address and address not in checked_url_set:
            print(address)
            checked_url_set.add(address)
            with open('urls.txt', 'ba') as file:
                file.write((address + '\n').encode('utf-8'))
            extract_links(base_url, address, checked_url_set)

def extract_link(url):
    extract_links(url, url, set())

    
extract_link(input("Enter your link: "))
