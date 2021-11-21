def register_api_urls(api):
    from .api.resources.ping import Ping
    from .api.resources.rates import RatesResource

    resources = [(Ping, "/ping"), (RatesResource, "/rates")]

    for resource_url in resources:
        api.add_resource(*resource_url)
