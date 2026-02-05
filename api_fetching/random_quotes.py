import requests

url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
response = requests.get(url)

if response.status_code != 200:
    raise Exception("Failed to fetch data")

data = response.json()

if data["success"]:
    user_data = data["data"]
    quote = user_data["content"]
    author = user_data["author"]
    modification_date = user_data["dateModified"]
    width= user_data["length"]

    print("Quote:")
    print(quote)
    print("\nAuthor:")
    print(author)
    print(modification_date)
    print(width)
else:
    raise Exception("Data not found")
