import requests
from send_email import send_email

api_key = "f2e37f1122ba4e31815adafbc7c780f2"

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-04-20&sortBy=publishedAt&apiKey=f2e37f1122ba4e31815adafbc7c780f2"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"
    
body = body.encode("utf-8") 
send_email(message=body)