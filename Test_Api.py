import requests
r = requests.post(
    "https://api.deepai.org/api/fast-style-transfer",
    data={
        'content': content_path,
        'style': style_path,
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())