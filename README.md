# dictnamespace
A very simple python structure to read/modify dictionary entries using attribute indexation


This is a very basic example of usage:

from dictnamespace import DictNamespace


data = {
    'port' : 80,
    'host' : 'localhost',
    'debug' : True,
    'logfile' : '/tmp/log.txt',
    'sites' : {
        'home' : {
            'endpoint' : 'index.php',
            'request-types' : ['GET', 'POST']
        }
    }
}

# We instantiate a DictNamespace object associated with the data dictionary
config = DictNamespace(data)

# Entries on the dictionary can be accessed using attribute indexation and also with the operator [] using DictNamespace object
# as a proxy
home = config.sites.home
print('[{}] http://{}:{}/{}'.format(
    ', '.join(home['request-types']),
    config.host,
    config.port,
    home.endpoint))
