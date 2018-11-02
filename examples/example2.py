

'''
Another example of DictNamespace usage. A dictionary called 'data' is first defined, then its passed as argument to
instantiate a DictNamespace object. Later, entries of such dictionary will be fetched using the DictNamespace object
'''

from dictnamespace import DictNamespace

if __name__ == '__main__':
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