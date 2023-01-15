from pymemcache import serde
from pymemcache.client.base import Client
import config

print('memcache initialization {0} {1}'.format(config.MEMCACHED_SERVER, config.MEMCACHED_PORT))
cache_client = Client((config.MEMCACHED_SERVER, config.MEMCACHED_PORT), serde=serde.pickle_serde)

