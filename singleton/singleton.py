import requests

class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        
        return cls._instances[cls]

class URLFetcher(metaclass=SingletonType):
    def fetch(self, url):
        resp = requests.get(url)
        if resp.status_code == 200:
            page = resp.content

            urls = self.urls
            urls.append(url)
            self.urls = urls

    def dump_url_registry(self):
        return ', '.join(self.urls)