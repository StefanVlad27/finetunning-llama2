import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
url = "https://www.3tres3.com/enfermedades/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
p_tags = soup.find_all('p', class_='fill')

data = []

for p in p_tags:
    a_tags = p.find_all('a', class_='titol colorLink')
    span_tags = p.find_all('span', class_='descripcio nota')
    for a, span in zip(a_tags, span_tags):
        source_text = a.get_text(strip=True)
        target_text = span.get_text(strip=True)

        source_target_pair = {
            "source": source_text,
            "target": target_text
        }
        data.append(source_target_pair)

# Name of the output JSONL file
output_file_name = "dataset.jsonl"

# Write data to JSONL file
with open(output_file_name, "w", encoding="utf-8") as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write("\n")

print("Web scraping and JSONL conversion completed.")
