import requests

r_sanfran = requests.get("https://api.angel.co/1/tags/1664/jobs").json()
num_pages = r_sanfran['last_page']

for page in range(2, num_pages + 1):
    r_sanfran = requests.get("https://api.angel.co/1/tags/1664/jobs", params={'page': page}).json()
    print r_sanfran['page']
    # TODO: extract the data
