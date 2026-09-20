from urllib.parse import quote
from .base import BaseService

class RisalaContentsService(BaseService):
    def __init__(self, baseurl: str, api_path: str):
        super().__init__()
        self.baseurl = baseurl
        self.api_path = api_path

    def getFullContents(self, params=None):
        if params is None:
            params = {}
        language = params.get("language", "en")
        lang = params.get("lang", "en")
        url = f"{self.baseurl}/{language}/{self.api_path}/get_full_contents?lang={lang}"
        return self._request(url)

    def getContents(self, params=None):
        if params is None:
            params = {}
        language = params.get("language", "en")
        lang = params.get("lang", "en")
        url = f"{self.baseurl}/{language}/{self.api_path}/content?lang={lang}"
        return self._request(url)

    def singleContent(self, content_id: int, language: str = "en"):
        url = f"{self.baseurl}/{language}/{self.api_path}/single-content?id={content_id}"
        return self._request(url)






class RisalaIslamicContentService(BaseService):
    def __init__(self, baseurl: str, api_path: str):
        super().__init__()
        self.baseurl = baseurl
        self.api_path = api_path

    def fatwas(self, params=None):
        if params is None:
            params = {}
        language = params.get("language", "en")
        lang = params.get("lang", "ar")
        is_featured = params.get("isFeatured", 1)
        url = f"{self.baseurl}/{language}/{self.api_path}/fatwas?lang={lang}&is_featured={is_featured}"
        return self._request(url)

    def hadeeths(self, params=None):
        if params is None:
            params = {}
        language = params.get("language", "en")
        lang = params.get("lang", "ar")
        is_featured = params.get("isFeatured", 1)
        url = f"{self.baseurl}/{language}/{self.api_path}/hadeeths?lang={lang}&is_featured={is_featured}"
        return self._request(url)

    def quran(self, params=None):
        if params is None:
            params = {}
        language = params.get("language", "en")
        lang = params.get("lang", "ar")
        is_featured = params.get("isFeatured", 1)
        url = f"{self.baseurl}/{language}/{self.api_path}/quran?lang={lang}&is_featured={is_featured}"
        return self._request(url)


class RisalaSearchService(BaseService):
    def __init__(self, baseurl: str, api_path: str):
        super().__init__()
        self.baseurl = baseurl
        self.api_path = api_path

    def contents(self, query: str, language: str = "en", page: int = 1):
        url = f"{self.baseurl}/{language}/{self.api_path}/search?query={quote(query)}&page={page}"
        return self._request(url)


class RisalaLookupsService(BaseService):
    def __init__(self, baseurl: str, api_path: str):
        super().__init__()
        self.baseurl = baseurl
        self.api_path = api_path

    def languages(self, language: str = "en", api_key: str = "A7X9G2L5M8P4T1C3D6V0KJQZRYBWFNSHEUO9682XLMTGVDPKJHQC7R5ZYA1B3W4F"):
        url = f"{self.baseurl}/{language}/{self.api_path}/langs?api_key={api_key}"
        return self._request(url)

    def contentTypes(self, language: str = "en"):
        url = f"{self.baseurl}/{language}/{self.api_path}/content-types"
        return self._request(url)


class RisalatAlHaramainService:
    def __init__(self):
        self.baseurl = "https://risala.prh.gov.sa"
        self.api_path = "Api"
        self.contents = RisalaContentsService(self.baseurl, self.api_path)
        self.islamicContent = RisalaIslamicContentService(self.baseurl, self.api_path)
        self.search = RisalaSearchService(self.baseurl, self.api_path)
        self.lookups = RisalaLookupsService(self.baseurl, self.api_path)
