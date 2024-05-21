import requests
from bs4 import BeautifulSoup as Bs

def get_html(url):
    respons = requests.get(url)
    if respons.status_code == 200:
        return respons.text
    return None

def get_data(html):
    soup = BS(html, "html.parser")
    container = soup.find("div", class_="container body-container")
    posts = container.find("div", class_="listing" itemscope="" itemtype="https://schema.org/Apartment" style="background: lineargradient(180deg, #FACC00 0%, #FFED9E 100%) ;">)
    
    links = []
    for post in posts:
        prices = post.find("div", class_="sep main")
        title = post.find("p", class_="title")
        location =post.find("div", class_="address")
        links = post.get("https://www.house.kg/kupit-kvartiru")
    return links

def get_posts(html):
    soup = BS(html, "html.parser")
    main = soup.find("div", class_="main content")


def main():
    URL = "https://www.house.kg/kupit-kvartiru"
    html = get_html(URL)
    links = get_links(html)
    for link in links:
        detail_html = get_html(link)
        data = get_posts(detail_html)


if __name__ == "__main__":
    main()













































