import importlib

req = importlib.import_module('requests')

s = req.get('https://www.facebook.com')
print(s.status_code)