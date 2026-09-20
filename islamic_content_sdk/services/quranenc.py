from .base import BaseService

class QuranencService(BaseService):
    def __init__(self):
        super().__init__()
        self.baseurl = "https://quranenc.com/api/v1"
        self.audio_base_url = "https://d.quranenc.com/data/audio"

    def translationList(self, params=None):
        if params is None:
            params = {}
        
        url = f"{self.baseurl}/translations/list"
        if params.get("language"):
            url += f"/{params['language']}"
        if params.get("localization"):
            url += f"?localization={params['localization']}"
            
        return self._request(url)

    def translationSura(self, translation_key: str, sura_number: int):
        url = f"{self.baseurl}/translation/sura/{translation_key}/{sura_number}"
        return self._request(url)

    def translationAya(self, translation_key: str, sura_number: int, aya_number: int):
        url = f"{self.baseurl}/translation/aya/{translation_key}/{sura_number}/{aya_number}"
        return self._request(url)

    def ayaAudio(self, translation_key: str, sura_number: int, aya_number: int):
        sura_3digits = str(sura_number).zfill(3)
        aya_3digits = str(aya_number).zfill(3)
        url = f"{self.audio_base_url}/{translation_key}/{sura_3digits}{aya_3digits}.mp3"
        return {
            "status": 200,
            "file_url": url,
            "content_type": "audio/mpeg"
        }


