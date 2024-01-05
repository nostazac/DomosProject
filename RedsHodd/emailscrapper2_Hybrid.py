import requests
import re

# Function to extract email addresses from the "Contact Us" page of a webpage
def extract_emails_from_contact_us(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            text = response.text
            # You may need to customize this regex to match the "Contact Us" page's structure
            contact_us_pattern = r'<a\s.*?href=[\'"](.*?contact.*?)["\'].*?>Contact Us</a>'
            match = re.search(contact_us_pattern, text, re.I)
            if match:
                contact_us_url = match.group(1)
                # Now, fetch the "Contact Us" page and extract emails
                contact_us_response = requests.get(contact_us_url)
                if contact_us_response.status_code == 200:
                    contact_us_text = contact_us_response.text
                    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                    emails = re.findall(email_pattern, contact_us_text)
                    return emails
    except Exception as e:
        print(f"Error while processing {url}: {str(e)}")
    return []

# List of URLs to process
url_list = [
    'https://kra.go.ke'
    # Add more URLs here
]

# File to save extracted email addresses
output_file = 'extracted_emails.txt'

# Extract and save emails
with open(output_file, 'w') as file:
    for url in url_list:
        emails = extract_emails_from_contact_us(url)
        if emails:
            for email in emails:
                file.write(email + '\n')

print(f"Email addresses extracted from {len(url_list)} 'Contact Us' pages and saved to {output_file}")
