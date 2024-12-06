import requests as req
from send_email import send_email

topic = "tesla"
api_key="b0f1d186a5ad4511988cc642a5b8657d"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-11-06&" \
      "sortBy=publishedAt&" \
      "apiKey=b0f1d186a5ad4511988cc642a5b8657d&" \
      "language=en"

#Make request
request=req.get(url)

#Get a dictionary with data
content = request.json()

print(type(content))

#Access the article titles and description and get only 4 articles
body=""
for article in content["articles"][0:20]:
    if body is not None:
       body = "Subject: Today's news " \
              + "\n" + body + article["title"] + \
              "\n" + article["description"] + \
              "\n" + article["url"] + 2*"\n"

body=body.encode("utf-8")
send_email(message=body)




