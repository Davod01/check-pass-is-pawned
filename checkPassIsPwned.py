import requests
import hashlib
import sys

pass_check_url = 'https://api.pwnedpasswords.com/range/'
result = []

def hash_pass(password):
  return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

def req_api_data(apiUrl,password):
  url = apiUrl + password
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res


def conver_to_list(res):
  return [ tp.split(':') for tp in res.splitlines() ]

def check_for_hash_password(resList,hPassword):
  for li in resList:
    if li[0] == hPassword:
      return (li[0],li[1])

# hashedPass = hash_pass(password)
# responseText = req_api_data(pass_check_url, hashedPass[:5] ).text

# result = check_for_hash_password(conver_to_list(responseText), hashedPass[5:])

# print( result )

def main(argv,url):
  for passwordPwned in argv:
    first5_char, tail = hash_pass(passwordPwned)[:5],hash_pass(passwordPwned)[5:]
    responseText = req_api_data(url, first5_char ).text
    result.append(check_for_hash_password(conver_to_list(responseText), tail))
  print(result)

main(sys.argv[1:],pass_check_url)