from api_auth_api import ApiAuthApi
from ..rest import ApiException
from pprint import pprint
from ..configuration import _fetch_credentials

# Create an instance of the API class
api_instance = ApiAuthApi()


def connect_to_api():
    client_id, client_secret, host = _fetch_credentials('lookerpy/config.yml', 'production')

    try:
        api_response = api_instance.login(client_id=client_id, client_secret=client_secret)

    except ApiException as e:
        pprint('Failed to connect to the Looker API: {}'.format(e))

    return api_response.access_token


if __name__ == '__main__':
    connect_to_api()
