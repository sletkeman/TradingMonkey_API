import requests
from requests_oauthlib import OAuth1, OAuth1Session
from urllib.parse import parse_qsl

BASE_URL="https://apisb.etrade.com/oauth" # Sandbox
PROD_BASE_URL="https://api.etrade.com/oauth"
AUTHORIZE_URL="https://us.etrade.com/e/t/etws/authorize"

def get_auth_url(consumer_key, consumer_secret):   
    auth_session = OAuth1Session(consumer_key, client_secret=consumer_secret, callback_uri='oob')
    response = auth_session.fetch_request_token(f"{BASE_URL}/request_token")
    auth_url = f"{AUTHORIZE_URL}?key={consumer_key}&token={response.get('oauth_token')}"
    return auth_url, response.get('oauth_token'), response.get('oauth_token_secret')

def get_auth_session(request_token, request_token_secret, text_code, consumer_key, consumer_secret):
    auth = OAuth1(consumer_key, consumer_secret, request_token, request_token_secret, verifier=text_code, signature_method='HMAC-SHA1')
    response = requests.get(f"{BASE_URL}/oauth/access_token", auth=auth)
    if response.status_code == 200:
        parsed = dict(parse_qsl(response.text))
        return parsed.get('oauth_token'), parsed.get('oauth_token_secret')
    else:
        raise Exception("Failed to get the access token")

def renew_session(consumer_key, consumer_secret, request_token, request_token_secret):
    auth = OAuth1(consumer_key, consumer_secret, request_token, request_token_secret, signature_method='HMAC-SHA1')
    response = requests.get(f'{BASE_URL}/renew_access_token', auth=auth)
    return response.status_code == 200