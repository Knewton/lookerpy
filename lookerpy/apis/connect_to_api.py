import yaml
from api_auth_api import ApiAuthApi
from ..rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = ApiAuthApi()

def fetch_credentials(configuration_yaml, environment):
    f = open(configuration_yaml)
    params = yaml.load(f)
    f.close()

    client_id = params[environment]['client_id']
    client_secret = params[environment]['client_secret']

    return client_id, client_secret

def connect_to_api():
    client_id, client_secret = fetch_credentials('config.yml', 'production')

    try:
        api_response = api_instance.login(client_id=client_id, client_secret=client_secret)

    except ApiException as e:
        pprint ('Failed to connect to the Looker API: {}'.format(e))

    return api_response.access_token

if __name__ == '__main__':
    connect_to_api()
