from nytimes_client import nytimes_client
import json

# client = nytimes_client()
# response = client.get_news()
# print(response)

# with open('data.json', 'w') as f:
#     json.dump(response.json(), f)

with open('data.json', 'r') as f:
    response = json.load(f)


for index, art in enumerate(response['response']['docs']):
    with open(f'{index}.json', 'w') as f:
        json.dump(art, f)