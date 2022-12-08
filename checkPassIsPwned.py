import requests
import hashlib
import sys

pass_check_url = 'https://api.pwnedpasswords.com/range/'

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
      return li[1]
  return ''

def pawned_password_message(myDict):
  if myDict["numberOfPawned"]:
    print(f'{myDict["password"]} was found {myDict["numberOfPawned"]} times... you shouldn`t use this password')
  else:
    print(f'{myDict["password"]} was not found. you can keep it up')


def main(argv,url):
  for password in argv:
    first5_char, tail = hash_pass(password)[:5],hash_pass(password)[5:]
    responseText = req_api_data(url, first5_char ).text
    listOfResponsedPass = conver_to_list(responseText)
    result = {"password":password,"numberOfPawned":check_for_hash_password(listOfResponsedPass, tail)}
    pawned_password_message(result)
  return "***  bye have great time  ***"

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:],pass_check_url))