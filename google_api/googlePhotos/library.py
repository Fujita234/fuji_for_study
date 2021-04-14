import requests, ast, urllib, json

code = '4/0AY0e-g6OOBE34DE9gjj17AAOLTKbc076EbCGNCHcTls9CIM6RkRE9I1PY-U5lf6PALHxsQ'
tokenpath = 'refresh_token.json'#保存したい場所

data = {
   'code': urllib.parse.unquote(code),
   'client_id': auth['client_id'],
   'client_secret': auth['client_secret'],
   'redirect_uri': auth['redirect_uris'][0],
   'grant_type': 'authorization_code',
   'access_type': 'offline'
}
response = requests.post('https://www.googleapis.com/oauth2/v4/token', data = data).json()
print(response)
if 'refresh_token' in response.keys():
   with open(topenpath, "w") as f:f.write(json.dumps(response))