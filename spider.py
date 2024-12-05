import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import argparse


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def extrair_urls(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        for tag_a in soup.find_all('a', href=True):
            link = urljoin(url, tag_a['href']) 
            if link.startswith("http"): 
                links.add(link)
        return links
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return set()


def crawler(url_inicial, visitados, dominio):
    print(f"Acessando: {url_inicial}")
    visitados.add(url_inicial)
    
 
    urls = extrair_urls(url_inicial)

    for url in urls:
       
        if url not in visitados and dominio in url:
            time.sleep(1)  
            crawler(url, visitados, dominio)

def main():
   
    parser = argparse.ArgumentParser(description="Crawler de Sites para extrair URLs")
    parser.add_argument("url", help="URL inicial para começar o crawler")
    
    args = parser.parse_args()

    url_inicial = args.url.strip()
    
    if not url_inicial.startswith("http"):
        url_inicial = "http://" + url_inicial  

    
    dominio = urlparse(url_inicial).netloc
    visitados = set()  

    crawler(url_inicial, visitados, dominio)

   
    with open("urls_coletadas.txt", "w") as arquivo:
        arquivo.write("\n".join(visitados))
    print(f"URLs coletadas salvas em 'urls_coletadas.txt'")

if __name__ == "__main__":
    main()
