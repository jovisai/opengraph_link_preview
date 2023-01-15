from cache import cache_client


def set_to_cache(key, value):
    cache_client.set('link_service_' + str(key), value)


def set_to_error(key):
    """
    the expiry will ensure I am able to retry the url later point in time in case the url is up again.
    currently setting the expiry to 60 secs
    :param key: any link
    :return: None
    """
    cache_client.set('link_service_error_' + str(key), "", expire=60)


def link_was_error(key):
    return cache_client.get('link_service_error_' + str(key)) is not None


def get_from_cache(key):
    return cache_client.get('link_service_' + str(key))


def remove_from_cache(key):
    cache_client.delete('link_service_' + str(key))
