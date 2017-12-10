#!/usr/bin/env python
import requests
from akamai.edgegrid import EdgeGridAuth
from urlparse import urljoin
from pprint import pprint


def auth(a_client_token, a_client_secret, a_access_token):
    session = requests.Session()
    session.auth = EdgeGridAuth(
        client_token=a_client_token,
        client_secret=a_client_secret,
        access_token=a_access_token
    )
    return session


def list_live_origins(session, baseurl):
    result = session.get(urljoin(baseurl, 'config-media-live/v1/msl-origin/origins'))
    return result.json()


if __name__ == "__main__":
    # Create variables for each key, secret, token
    client_secret = os.environ['CLIENT_SECRET']
    client_token = os.environ['CLIENT_TOKEN']
    access_token = os.environ['ACCESS_TOKEN']
    host = os.environ['API_HOST']
    baseurl = 'https://{}'.format(host)

    s = auth(client_token, client_secret, access_token)
    origins = list_live_origins(s, baseurl)
    pprint(origins)
