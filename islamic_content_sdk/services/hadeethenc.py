from urllib.parse import urlencode
from .base import BaseService

class HadeethencService(BaseService):
    def __init__(self):
        super().__init__()
        self.baseurl = "https://hadeethenc.com/api/v1"

    def languages(self):
        url = f"{self.baseurl}/languages"
        return self._request(url)

    def categories(self, language_code: str, parent_id: int = None):
        query = urlencode({"language": language_code})
        url = f"{self.baseurl}/categories/list/?{query}"
        result = self._request(url)
        if parent_id is not None and isinstance(result, list):
            return [c for c in result if str(c.get("parent_id")) == str(parent_id)]
        return result

    def rootCategories(self, language_code: str):
        query = urlencode({"language": language_code})
        url = f"{self.baseurl}/categories/roots/?{query}"
        return self._request(url)

    def hadithsList(self, params: dict):
        query_params = {"language": params["language"]}
        if params.get("categoryId") is not None:
            query_params["category_id"] = params["categoryId"]
        if params.get("page") is not None:
            query_params["page"] = params["page"]
        if params.get("perPage") is not None:
            query_params["per_page"] = params["perPage"]

        query = urlencode(query_params)
        url = f"{self.baseurl}/hadeeths/list/?{query}"
        return self._request(url)

    def hadithDetails(self, params: dict):
        query_params = {
            "id": params["id"],
            "language": params["language"]
        }
        query = urlencode(query_params)
        url = f"{self.baseurl}/hadeeths/one/?{query}"
        return self._request(url)
