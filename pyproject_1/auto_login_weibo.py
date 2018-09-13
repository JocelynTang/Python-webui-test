import requests,sys
import os


r = requests.get('https://weibo.com')
print r.status_code
print r.headers
