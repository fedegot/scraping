import requests

url = "https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"

response = requests.get(url)


prop = "Previous Close"
"""print(response)"""
"""print(response.status_code==200)"""
t = response.text



ind = t.index("Previous Close")
mm = t[ind:].split("</td>")[1]
val = mm.split("</td>")[-1].split()
val2 = val[4]
print(val2[-8:])
