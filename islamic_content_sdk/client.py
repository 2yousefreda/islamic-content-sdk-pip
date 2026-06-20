from .services.quranenc import QuranencService
from .services.hadeethenc import HadeethencService
from .services.islamhouse import IslamhouseService
from .services.risalat_al_haramain import RisalatAlHaramainService
from .services.bayan_al_islam import BayanAlIslamService
from .services.al_montaka import AlMontakaService

class IslamicContentSdk:
    def __init__(self):
        self.quranenc = QuranencService()
        self.hadeethenc = HadeethencService()
        self.islamhouse = IslamhouseService()
        self.risalatAlHaramain = RisalatAlHaramainService()
        self.bayanAlIslam = BayanAlIslamService()
        self.alMontaka = AlMontakaService()
