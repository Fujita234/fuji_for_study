import requests, ast, urllib, json

filepath = 'client_secret_601839991339-6kfcr8qbgva8cm8k4qjog2r6qt1fc946.apps.googleusercontent.com.json'

# ここで認証してもらう
with open(filepath) as f:txt = f.read()
auth = ast.literal_eval(txt)['web']
SCOPE ='https://www.googleapis.com/auth/photoslibrary'
url = "https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=%s&redirect_uri=%s&scope=%s&access_type=offline" % (auth['client_id'], auth['redirect_uris'][0], SCOPE)
# print(url)


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
   with open(tokenpath, "w") as f:f.write(json.dumps(response))