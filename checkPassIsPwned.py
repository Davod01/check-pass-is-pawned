import requests
import hashlib

pass_check_url = 'https://api.pwnedpasswords.com/range/'
password = 'q123456w'
myResponse = None
responseText = None

def hash_pass(password):
  return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

def req_api_data(apiUrl,password):
  url = apiUrl + password
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res


def conver_to_tuple(res):
  return [ tuple(tp.split(':')) for tp in res.splitlines() ]

hashedPass = hash_pass(password)
myResponse = req_api_data(pass_check_url, hashedPass[:5] )
responseText = myResponse.text

print( conver_to_tuple(responseText) )