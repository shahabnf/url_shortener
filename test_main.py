from urllib import response
from urlshort import create_app

def test_shorten(client):
    response = client.get('/')              # respone is home page 
    assert b'Shorten' in response.data      # find Shorten text in our web page