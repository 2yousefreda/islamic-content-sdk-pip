import json
from urllib.parse import urlencode, quote
from .base import BaseService

class BayanAlIslamService(BaseService):
    def __init__(self):
        super().__init__()
        self.baseurl = "https://byenah.com"

    def languagesList(self, language: str = "ar"):
        url = f"{self.baseurl}/{language}/Api/languages/list"
        return self._request(url)

    def muslimList(self, language: str = "en", page: int = 1):
        url = f"{self.baseurl}/{language}/Api/content/muslims/full_list?page={page}"
        return self._request(url)

    def nonMuslimList(self, language: str = "en", page: int = 1):
        url = f"{self.baseurl}/{language}/Api/content/non-muslims/full_list?page={page}"
        return self._request(url)



    def paginatedLanguages(self, params=None):
        if params is None:
            params = {}
        language = params.get("language", "en")
        query_params = {}
        if params.get("name"):
            query_params["name"] = params["name"]
        if params.get("page") is not None:
            query_params["page"] = params["page"]
        
        query = urlencode(query_params)
        url = f"{self.baseurl}/{language}/Api/paginated-languages?{query}"
        return self._request(url)

    def recentContents(self, params: dict):
        language = params.get("language", "en")
        query_params = {
            "lang": params["lang"],
            "init": str(params["init"]).lower()
        }
        if params.get("ids") and len(params["ids"]) > 0:
            query_params["ids"] = json.dumps(params["ids"])

        query = urlencode(query_params)
        url = f"{self.baseurl}/{language}/Api/recent-contents?{query}"
        return self._request(url)

    def lookups(self, language: str = "en"):
        url = f"{self.baseurl}/{language}/Api/lookups"
        return self._request(url)

    def nameSearch(self, name: str, language: str = "ar"):
        url = f"{self.baseurl}/{language}/Api/name_search?name={quote(name)}"
        return self._request(url)


