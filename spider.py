import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

HEADERS = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def extration_url(url):
    
    try:
        response = requests.get(url,headers=HEADERS, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        links = set()

        for tag_a in soup.find_all('a', href=True):
            link = urljoin(url, tag_a['href'])
            if link.startswith("http"):
                link.add(link)
    
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error ao acessar {url} : {e}")
        return
            

