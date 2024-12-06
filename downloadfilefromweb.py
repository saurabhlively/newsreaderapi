import requests as req



url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Town_Hall%2C_Yarmouth%2C_England-LCCN2002708291_-_Restoration.jpg/600px-Town_Hall%2C_Yarmouth%2C_England-LCCN2002708291_-_Restoration.jpg"

response = req.get(url)
content = response.content

with open("image.jpg","wb") as file:
    file.write(content)