from cache import cache_client


def set_to_cache(key, value):
    cache_client.set('link_service_' + str(key), value)


def get_from_cache(key):
    return cache_client.get('link_service_' + str(key))


def remove_from_cache(key):
    cache_client.delete('link_service_' + str(key))
