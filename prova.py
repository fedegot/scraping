import requests

url = "https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"

response = requests.get(url)


prop = "Previous Close"
"""print(response)"""
"""print(response.status_code==200)"""
t = response.text



ind = t.index("Previous Close")
print(t[ind:ind+200])