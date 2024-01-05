import requests
from bs4 import BeautifulSoup

# Define the URL to start crawling from
start_url = input(' Enter url in form **https://example.com')

# Create a list to store visited URLs
visited_urls = []

# Define a function to crawl a URL
def crawl(url):
    if url not in visited_urls:
        try:
            # Send an HTTP GET request to the URL
            response = requests.get(url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the page content using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract and print the page title
                page_title = soup.title.string
                print(f'Title: {page_title}')
                
                # Extract and print all the links on the page
                for link in soup.find_all('a'):
                    link_url = link.get('href')
                    if link_url and link_url.startswith('http'):
                        print(f'Link: {link_url}')
                
                # Mark this URL as visited
                visited_urls.append(url)
                
                # Recursively crawl linked pages
                for link in soup.find_all('a'):
                    link_url = link.get('href')
                    if link_url and link_url.startswith('http'):
                        crawl(link_url)
        except Exception as e:
            print(f"Error crawling {url}: {e}")

# Start crawling
crawl(start_url)
