import requests  #IMPORT REQUESTS

r = requests.get('http://www.geeksforgeeks.org/python-programming-language/')

print(r)

print(r._content)