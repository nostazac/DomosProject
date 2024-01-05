import requests
from bs4 import BeautifulSoup

def get_web_content(url):
    
    try:
        response = requests.get(url)
        response.raise_for_status() # raise HTTOError for bad response
        
        return response.text
    
    except requests.exceptions.RequestException as e:
        
        print(f"Error: {e}")
        
        return None
def extract_links(html_content):
    
    links = []
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for a_tag in soup.find_all('a', href = True):
        links.append(a_tag['href'])
        
    return links

def main():
    target_url = input("Enter the target URL: ")
    
    # Ensure the URL starts with https:// or http://
    if not target_url.startswith(("http://", "https://")):
        
        target_url = get_web_content(target_url)
        
    web_content = get_web_content(target_url)
    
    if web_content:
        print(f"\n Web Content for {target_url}:\n{web_content}")
        
        links = extract_links(web_content)
        print("\nExtracted Links: ")
        
        for link in links:
            print(link)
            
if __name__ == "__main__":
    main()