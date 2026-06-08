import json

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.thereporterethiopia.com"

response = requests.get(
    url, 
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)
print(response.status_code)


soup = BeautifulSoup(response.text,"html.parser")

# headlines = []
# for article in soup.find_all("h2"):
#     title = article.get_text(strip=True)
#     if title:
#         headlines.append(
#             {
#                 "title": title
#             }
#         )

# print("Collected:", len(headlines))
# df = pd.DataFrame(headlines)
# df.to_csv(
#     "ethiopian_news.csv",
#     index=False
# )

# print(df.head())
   

data = []

articles = soup.find_all("a")

for article in articles:
    title = article.get_text(strip=True)
    href = article.get("href")

    if not title or not href:
        continue

    # remove junk text
    if len(title) < 25:
        continue

    if "reporter ethiopia" in title.lower():
        continue

    if href.startswith("/"):
        href = "https://www.thereporterethiopia.com" + href

    data.append({
        "title": title,
        "url": href
    })
    
print("Collected:", len(data))

#save csv
df = pd.DataFrame(data)
df.to_csv(
    "ethiopian_news.csv",
    index=False
)

#save JSON 
with open("ethiopian_news.json", "w", encoding="utf-8") as f:
   json.dump(data, f, ensure_ascii=False, indent=4)
print("Saved csv + JSON sucessfully")

