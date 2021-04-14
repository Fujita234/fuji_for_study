import sys
import requests
import json

def main():
  url = "https://www.google.co.jp/search"
  params = {'q': '日本代表', 'tbm': 'nws'}
  r = requests.get(url, params)
  print(r["hash"])

def main_2():
  base_url = "https://yesno.wtf/api"
  # GET通信でリクエストを送り、レスポンスを受け取る
  response = requests.get(base_url).json()

  # レスポンスはJSON 読み込む
  print(response)


main()
main_2()