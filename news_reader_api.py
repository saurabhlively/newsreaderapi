import requests as req
from send_email import send_email


api_key="b0f1d186a5ad4511988cc642a5b8657d"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-11-06&sortBy=publishedAt&apiKey=b0f1d186a5ad4511988cc642a5b8657d"

#Make request
request=req.get(url)

#Get a dictionary with data
content = request.json()

print(type(content))

#Access the article titles and description
body=""
for article in content["articles"]:
    if body is not None:
       body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body=body.encode("utf-8")
send_email(message=body)




