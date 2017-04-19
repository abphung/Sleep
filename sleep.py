import fitbit
import json
import datetime
from gather_keys_oauth2 import OAuth2Server

client_id = '2283V9'
client_secret = 'a18296c1411eadab772a3d9d7dc44112'

server = OAuth2Server(client_id, client_secret)
server.browser_authorize()

token = server.fitbit.client.session.token.items()
print token

access_token = token['access_token']
refresh_token = token['refresh_token']
user_id = token['user_id']
auth_client = fitbit.Fitbit(client_id, client_secret, access_token = access_token, refresh_token = refresh_token)
data = auth_client.sleep(date = datetime.datetime.today() - datetime.timedelta(days = 1), user_id = user_id)['sleep'][0]
print data.keys()
