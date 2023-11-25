#-------------------------------------------------------------------------
# AUTHOR: Tim Hsieh
# FILENAME: crawler.py
# SPECIFICATION: reads the CS faculty information, parses faculty members information and collects in MongoDB
# FOR: CS 4250- Assignment #3
# TIME SPENT: 5 hours
#-----------------------------------------------------------*/

from pymongo import MongoClient
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def connectDataBase():
    client = MongoClient("mongodb://localhost:27017")  
    db = client["CrawlerDB"]
    print("Database is connected.")
    return db

def getPageLink(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        absolute_url = urljoin(url, href)
        links.append(absolute_url)

    return links

def findHeading(url, target):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    storePage(url, soup.prettify())
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for heading in headings:
        if target.lower() in heading.text.lower():
            return True

    return False

def crawlerThread(initial_url, target):
    visited_urls = set()
    urls_to_visit = [initial_url]

    while urls_to_visit:
        current_url = urls_to_visit.pop(0)

        if current_url in visited_urls:
            continue

        visited_urls.add(current_url)

        if findHeading(current_url, target):
            print(f'Found "{target}" at: {current_url}')
            return

        new_links = getPageLink(current_url)
        urls_to_visit.extend(new_links)

def storePage(url, html):
    pages = db.pages
    page = {
        "url": url,
        "html": html
    }

    pages.insert_one(page)

if __name__ == "__main__":
    initial_url = "https://www.cpp.edu/sci/computer-science/"
    target = "Permanent Faculty"
    db = connectDataBase()
    
    crawlerThread(initial_url, target)