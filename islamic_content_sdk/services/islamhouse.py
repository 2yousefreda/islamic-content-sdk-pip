from .base import BaseService

class IslamhouseCategoriesAndTypesService(BaseService):
    def __init__(self, baseurl: str):
        super().__init__()
        self.baseurl = baseurl

    def allTypes(self, site_lang: str, content_lang: str):
        url = f"{self.baseurl}/main/sitecontent/{site_lang}/{content_lang}/json"
        return self._request(url)

    def allCategories(self, language: str):
        url = f"{self.baseurl}/categories/showall/{language}/json"
        return self._request(url)

    def categoriesTree(self, language: str):
        url = f"{self.baseurl}/main/get-object-category-tree/{language}/json"
        return self._request(url)

    def childCategories(self, category_id: int, site_lang: str, content_lang: str):
        url = f"{self.baseurl}/categories/viewcat/{category_id}/{site_lang}/{content_lang}/json"
        return self._request(url)

    def singleCategoryBasic(self, category_id: int, language: str):
        url = f"{self.baseurl}/categories/viewitem/{category_id}/{language}/json"
        return self._request(url)

    def subCategories(self, category_id: int, language: str):
        url = f"{self.baseurl}/main/get-sub-categories/{category_id}/{language}/json"
        return self._request(url)

    def categoryTypes(self, category_id: int, site_lang: str, content_lang: str):
        url = f"{self.baseurl}/main/get-category-types-available/{category_id}/{site_lang}/{content_lang}/json"
        return self._request(url)

    def categoryLanguages(self, category_id: int, slang: str, language: str):
        url = f"{self.baseurl}/main/get-category-source-languages/{category_id}/{slang}/{language}/json"
        return self._request(url)


class IslamhouseItemsService(BaseService):
    def __init__(self, baseurl: str):
        super().__init__()
        self.baseurl = baseurl

    def listItems(self, type: str, site_lang: str, slang: str, page: int = 1, limit: int = 25):
        url = f"{self.baseurl}/main/{type}/{site_lang}/{slang}/{page}/{limit}/json"
        return self._request(url)

    def authorItems(self, author_id: int, slang: str, site_lang: str, content_lang: str, page: int = 1, limit: int = 20):
        url = f"{self.baseurl}/main/get-author-items/{author_id}/{slang}/{site_lang}/{content_lang}/{page}/{limit}/json"
        return self._request(url)

    def categoryItems(self, category_id: int, slang: str, site_lang: str, content_lang: str, page: int = 1, limit: int = 20):
        url = f"{self.baseurl}/main/get-category-items/{category_id}/{slang}/{site_lang}/{content_lang}/{page}/{limit}/json"
        return self._request(url)

    def latestItems(self, period: str, slang: str, site_lang: str, content_lang: str, page: int = 1, limit: int = 25):
        url = f"{self.baseurl}/main/get-latest/{period}/{slang}/{site_lang}/{content_lang}/{page}/{limit}/json"
        return self._request(url)

    def highlightedItems(self, site_lang: str, content_lang: str):
        url = f"{self.baseurl}/main/get-highlights/{site_lang}/{content_lang}/json"
        return self._request(url)

    def itemsCount(self, type: str, site_lang: str, content_lang: str):
        url = f"{self.baseurl}/main/get-language-items-count/{type}/{site_lang}/{content_lang}/json"
        return self._request(url)


class IslamhouseItemService(BaseService):
    def __init__(self, baseurl: str):
        super().__init__()
        self.baseurl = baseurl

    def details(self, item_id: int, language: str):
        url = f"{self.baseurl}/main/get-item/{item_id}/{language}/json"
        return self._request(url)

    def attachments(self, item_id: int):
        url = f"{self.baseurl}/main/check-attachment/{item_id}/json"
        return self._request(url)

    def tree(self, item_id: int, language: str):
        url = f"{self.baseurl}/main/get-item-tree/{item_id}/{language}/json"
        return self._request(url)

    def cardTranslations(self, item_id: int, language: str):
        url = f"{self.baseurl}/main/get-item-card-translations/{item_id}/{language}/json"
        return self._request(url)

    def translations(self, item_id: int, language: str):
        url = f"{self.baseurl}/main/get-item-translations/{item_id}/{language}/json"
        return self._request(url)


class IslamhouseAuthorsService(BaseService):
    def __init__(self, baseurl: str):
        super().__init__()
        self.baseurl = baseurl

    def list(self, params=None):
        if params is None:
            params = {}
        kind = params.get("kind", "showall")
        locale = params.get("locale", "showall")
        sort = params.get("sort", "countdesc")
        page = params.get("page", 1)
        per_page = params.get("perPage", 20)

        url = f"{self.baseurl}/main/get-authors-data/{kind}/{locale}/{sort}/{page}/{per_page}/json"
        return self._request(url)

    def details(self, author_id: int, language: str):
        url = f"{self.baseurl}/main/get-author/{author_id}/{language}/json"
        return self._request(url)

    def cardTranslations(self, author_id: int, language: str):
        url = f"{self.baseurl}/main/get-author-card-translations/{author_id}/{language}/json"
        return self._request(url)

    def availableTypes(self, author_id: int, site_lang: str, content_lang: str):
        url = f"{self.baseurl}/main/get-author-types-avaliable/{author_id}/{site_lang}/{content_lang}/json"
        return self._request(url)

    def availableLocales(self, author_id: int, slang: str, language: str):
        url = f"{self.baseurl}/main/get-author-available-languages/{author_id}/{slang}/{language}/json"
        return self._request(url)


class IslamhouseLanguagesService(BaseService):
    def __init__(self, baseurl: str):
        super().__init__()
        self.baseurl = baseurl

    def keys(self):
        url = f"{self.baseurl}/languages/get-language-details/json"
        return self._request(url)

    def terms(self, language: str):
        url = f"{self.baseurl}/languages/get-language-terms/{language}/json"
        return self._request(url)

    def availableLanguages(self, slang: str, language: str):
        url = f"{self.baseurl}/main/get-available-languages/{slang}/{language}/json"
        return self._request(url)


class IslamhouseQuranService(BaseService):
    def __init__(self, baseurl: str):
        super().__init__()
        self.baseurl = baseurl

    def categories(self, language: str):
        url = f"{self.baseurl}/quran/get-categories/{language}/json"
        return self._request(url)

    def singleCategory(self, category_id: int, language: str):
        url = f"{self.baseurl}/quran/get-category/{category_id}/{language}/json"
        return self._request(url)

    def authorDetails(self, author_id: int, language: str):
        url = f"{self.baseurl}/quran/get-author/{author_id}/{language}/json"
        return self._request(url)

    def authorRecitations(self, author_id: int, language: str):
        url = f"{self.baseurl}/quran/get-author-recitations/{author_id}/{language}/json"
        return self._request(url)

    def suraDetails(self, sura_id: int, language: str):
        url = f"{self.baseurl}/quran/get-sura/{sura_id}/{language}/json"
        return self._request(url)

    def suraRecitations(self, sura_id: int, language: str):
        url = f"{self.baseurl}/quran/get-sura-recitations/{sura_id}/{language}/json"
        return self._request(url)

    def recitationDetails(self, recitation_id: int, language: str):
        url = f"{self.baseurl}/quran/get-recitation/{recitation_id}/{language}/json"
        return self._request(url)


class IslamhouseService:
    def __init__(self):
        self.baseurl = "https://api3.islamhouse.com/v3/paV29H2gm56kvLPy"
        self.categoriesAndTypes = IslamhouseCategoriesAndTypesService(self.baseurl)
        self.items = IslamhouseItemsService(self.baseurl)
        self.item = IslamhouseItemService(self.baseurl)
        self.authors = IslamhouseAuthorsService(self.baseurl)
        self.languages = IslamhouseLanguagesService(self.baseurl)
        self.quran = IslamhouseQuranService(self.baseurl)
