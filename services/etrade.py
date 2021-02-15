from rauth import OAuth1Service

def get_auth_url():
    etrade = OAuth1Service(
        name="etrade",
        consumer_key="3f4aa7259e9664017a45b5d86045fcad",
        consumer_secret="967853488874ed2d98e993d542658e222b729d3931feeaa9e91872f04cc70afb",
        request_token_url="https://api.etrade.com/oauth/request_token",
        access_token_url="https://api.etrade.com/oauth/access_token",
        authorize_url="https://us.etrade.com/e/t/etws/authorize?key={}&token={}",
        base_url="https://apisb.etrade.com")
    
    request_token, request_token_secret = etrade.get_request_token(
        params={"oauth_callback": "oob", "format": "json"})
    
    authorize_url = etrade.authorize_url.format(etrade.consumer_key, request_token)
    
    return authorize_url, request_token_secret

def get_auth_session(request_token, request_token_secret, text_code):
    etrade = OAuth1Service(
        name="etrade",
        consumer_key="3f4aa7259e9664017a45b5d86045fcad",
        consumer_secret="967853488874ed2d98e993d542658e222b729d3931feeaa9e91872f04cc70afb",
        request_token_url="https://api.etrade.com/oauth/request_token",
        access_token_url="https://api.etrade.com/oauth/access_token",
        authorize_url="https://us.etrade.com/e/t/etws/authorize?key={}&token={}",
        base_url="https://apisb.etrade.com")
    
    session = etrade.get_auth_session(request_token,
                                  request_token_secret,
                                  params={"oauth_verifier": text_code})
    
    return session