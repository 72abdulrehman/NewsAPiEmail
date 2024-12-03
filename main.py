import requests
from send_email import send_email

topic = "tesla"
api_key = ""
url = "https://newsapi.org/v2/everything?"\
        f"q={topic}&from=2024-04-20&sortBy=publishedAt&"\
        "apiKey=f2e37f1122ba4e31815adafbc7c780f2"\
        "&language=en"

# Making Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article features
body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    body = body + article["title"] + "\n" \
        + str(article["description"]) \
        + "\n" + article["url"] + 2*"\n"
    
body = body.encode("utf-8") 
send_email(message=body)
