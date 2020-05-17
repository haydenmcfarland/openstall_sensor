from os import environ

API_HOST = environ.get('OPENSTALL_API_HOST', '192.168.1.28')
API_PORT = environ.get('OPENSTALL_API_PORT', 3000)
API_PATH = environ.get('OPENSTALL_API_PATH', 'graphql')
API_URL = 'http://{}:{}/{}'.format(API_HOST, API_PORT, API_PATH)
ERROR_QUERY = "Query failed to run by returning code of {}. {}"
PIR_PIN = 4
SLEEP = 100
