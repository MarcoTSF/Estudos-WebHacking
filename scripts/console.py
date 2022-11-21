import requests
import datetime 
import json 
import urllib 

session_data = {
    'sessionId': '[AWS_ACCESS_KEY_ID]',
    'sessionKey': '[AWS_SECRET_ACCESS_KEY]',
    'sessionToken': '[AWS_SESSION_TOKEN]'
}
aws_federated_signin_endpoint = 'https://signin.aws.amazon.com/federation'

# Make a request to the AWS federation endpoint to get a sign-in token.
# The requests.get function URL-encodes the parameters and builds the query string
# before making the request.
response = requests.get(
    aws_federated_signin_endpoint,
    params={
        'Action': 'getSigninToken',
        'SessionDuration': str(datetime.timedelta(hours=12).seconds),
        'Session': json.dumps(session_data)
    })
try:
    signin_token = json.loads(response.text)
    print(f"Got a sign-in token from the AWS sign-in federation endpoint.")

    # Make a federated URL that can be used to sign into the AWS Management Console.
    query_string = urllib.parse.urlencode({
        'Action': 'login',
        'Issuer': '',
        'Destination': 'https://console.aws.amazon.com/',
        'SigninToken': signin_token['SigninToken']
    })
    federated_url = f'{aws_federated_signin_endpoint}?{query_string}'
    print(federated_url)
except:
    print("Ooops, something went wrong. Check your credentials and try again.")