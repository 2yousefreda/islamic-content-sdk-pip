from urllib.parse import urlencode
from .base import BaseService

class AlMontakaContentsService(BaseService):
    def __init__(self, baseurl: str):
        super().__init__()
        self.baseurl = baseurl

    def list(self, page: int = 1, categories: list = None):
        query_params = {"page": str(page)}
        if categories and len(categories) > 0:
            for index, cat in enumerate(categories):
                query_params[f"category[{index}]"] = str(cat)
        query = urlencode(query_params)
        url = f"{self.baseurl}/content?{query}"
        return self._request(url)

    def comments(self, content_id: int):
        url = f"{self.baseurl}/comments?content_id={content_id}"
        return self._request(url)

    def addComment(self, content_id: int, comment: str):
        url = f"{self.baseurl}/comment"
        body = {
            "content_id": str(content_id),
            "comment": comment
        }
        return self._request(
            url,
            "POST",
            body,
            {"Content-Type": "application/x-www-form-urlencoded"}
        )




class AlMontakaLookupsService(BaseService):
    def __init__(self, baseurl: str):
        super().__init__()
        self.baseurl = baseurl

    def ageGroups(self):
        url = f"{self.baseurl}/age-groups"
        return self._request(url)

    def categories(self, params: dict):
        query_params = {
            "language_id": str(params["languageId"]),
            "name_cont": params["nameCont"]
        }
        query = urlencode(query_params)
        url = f"{self.baseurl}/categories?{query}"
        return self._request(url)

    def entities(self, params: dict):
        query_params = {
            "language_id": str(params["languageId"]),
            "name_cont": params["nameCont"]
        }
        query = urlencode(query_params)
        url = f"{self.baseurl}/entities?{query}"
        return self._request(url)

    def expertLevels(self, params: dict):
        query_params = {
            "language_id": str(params["languageId"]),
            "name_cont": params["nameCont"]
        }
        query = urlencode(query_params)
        url = f"{self.baseurl}/expert-levels?{query}"
        return self._request(url)

    def ideologies(self, params: dict):
        query_params = {
            "language_id": str(params["languageId"]),
            "name_cont": params["nameCont"],
            "parent_id": str(params["parentId"])
        }
        query = urlencode(query_params)
        url = f"{self.baseurl}/ideologies?{query}"
        return self._request(url)

    def languages(self):
        url = f"{self.baseurl}/languages"
        return self._request(url)

    def persons(self, params=None):
        if params is None:
            params = {}
        query_params = {}
        if params.get("nameCont"):
            query_params["name_cont"] = params["nameCont"]
        if params.get("page") is not None:
            query_params["page"] = params["page"]
        
        query = urlencode(query_params)
        url = f"{self.baseurl}/persons?{query}"
        return self._request(url)

    def sections(self, params: dict):
        query_params = {
            "language_id": str(params["languageId"]),
            "name_cont": params["nameCont"]
        }
        query = urlencode(query_params)
        url = f"{self.baseurl}/sections?{query}"
        return self._request(url)

    def tags(self, params: dict):
        query_params = {
            "language_id": str(params["languageId"]),
            "name_cont": params["nameCont"]
        }
        query = urlencode(query_params)
        url = f"{self.baseurl}/tags?{query}"
        return self._request(url)

    def targetedGroups(self):
        url = f"{self.baseurl}/targeted-groups"
        return self._request(url)

    def youtubeChannels(self):
        url = f"{self.baseurl}/youtube-channels"
        return self._request(url)


class AlMontakaService:
    def __init__(self):
        self.baseurl = "https://content.mofeed.org/Api"
        self.contents = AlMontakaContentsService(self.baseurl)
        self.lookups = AlMontakaLookupsService(self.baseurl)
