import requests as req



api_key="b0f1d186a5ad4511988cc642a5b8657d"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-11-06&sortBy=publishedAt&apiKey=b0f1d186a5ad4511988cc642a5b8657d"

#Make request
request=req.get(url)

#Get a dictionary with data
content = request.json()

print(type(content))

#Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])


