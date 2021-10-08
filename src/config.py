from os import environ 

def get(name):
    return environ.get(name)

POSTGRES_USER = get('POSTGRES_USER')
POSTGRES_PASSWORD = get('POSTGRES_PASSWORD')
POSTGRES_DB = get('POSTGRES_DB')
POSTGRES_HOSTNAME = get('POSTGRES_HOSTNAME')
POSTGRES_PORT = get('POSTGRES_PORT')

