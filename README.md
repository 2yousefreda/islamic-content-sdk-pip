# Islamic Content SDK (Python)

An integrated and easy-to-use software library for Python developers to fetch authentic Islamic content (The Holy Qur'an and Hadith) in multiple languages directly from official sources.

This project is developed for [The Association for Multi-lingual Islamic Content](https://islamiccontent.sa/).

---

## Services Overview

This SDK aggregates content from multiple major multi-lingual Islamic platforms:

- **QuranEnc (`quranenc`)**: Quran Translations, suras, verses, and audios.
- **HadeethEnc (`hadeethenc`)**: Hadith collections, category trees, and grades.
- **IslamHouse (`islamhouse`)**: Multi-lingual books, articles, audios, fatwas, and author details.
- **Risalat Al-Haramain (`risalatAlHaramain`)**: Platform content, Fatwas, Quran recitations, and Hadiths.
- **Bayan Al Islam (`bayanAlIslam`)**: Educational booklets and resources tailored for Muslims and Non-Muslims.
- **Al Montaka (`alMontaka`)**: Structured lookups, categories, content filters, and community comments.

---

## Installation

Install the package via pip:

```bash
pip install islamic-content-sdk
```

## Usage

### Initializing the SDK

```python
from islamic_content_sdk import IslamicContentSdk

sdk = IslamicContentSdk()
```

---

## Detailed Service Methods Reference

Below is a complete guide on how to interact with every single method and option available in the SDK.

### Quran Source (QuranEnc API)

**API Documentation Link:** [QuranEnc API](https://quranenc.com/en/home/api/)

```python
# 1. Get available translations list on the platform
translations = sdk.quranenc.translationList({
    "language": "es",      # Optional: Filter list by language code
    "localization": "ar"   # Optional: Localize names in the response
})

# 2. Translate an entire sura (Al-Fatiha in Spanish)
sura = sdk.quranenc.translationSura("spanish_montada_eu", 1)

# 3. Translate a specific verse (Ayah 1 of Sura 1)
aya = sdk.quranenc.translationAya("spanish_montada_eu", 1, 1)

# 4. Get the audio MP3 file details for a specific verse
audio = sdk.quranenc.ayaAudio("chinese_suliman", 1, 1)
# Returns: {"status": 200, "file_url": "...", "content_type": "audio/mpeg"}

# 5. Submit translation feedback/note (POST request)
note_response = sdk.quranenc.addNote({
    "sura": 1,
    "aya": 1,
    "name": "QA Tester",
    "email": "qa@example.com",
    "note": "Test note from SDK automated test suite",
    "translation_key": "spanish_montada_eu",
    "source": "sdk_test",
    "version": "1.0.0",
    "suggested_translation": "Suggested text" # Optional
})
```

---

### Hadith Source (HadeethEnc API)

**API Documentation Link:** [HadeethEnc API](https://documenter.getpostman.com/view/5211979/TVev3j7q#intro)

```python
# 1. Get available languages in the encyclopedia
languages = sdk.hadeethenc.languages()

# 2. Get all categories of Hadith translated in a specific language
categories = sdk.hadeethenc.categories("en")

# 3. Get main (root) categories of Hadith in English
root_categories = sdk.hadeethenc.rootCategories("en")

# 4. List Hadiths under a category with pagination
hadiths = sdk.hadeethenc.hadithsList({
    "language": "en",
    "categoryId": 1,  # Optional: Category ID
    "page": 1,        # Optional: Page number
    "perPage": 20     # Optional: Number of items per page
})

# 5. Get full explanation, translations, and grade of a specific Hadith by ID
hadith = sdk.hadeethenc.hadithDetails({
    "id": 2962,
    "language": "ar"
})
```

---

### IslamHouse Source (IslamHouse v3 API)

**API Documentation Link:** [IslamHouse API Docs](https://documenter.getpostman.com/view/7929737/TzkyMfPc)

```python
# ==========================================
# 1. Categories & Types (categoriesAndTypes)
# ==========================================

# Core material types (videos, books, fatwas, etc.)
types = sdk.islamhouse.categoriesAndTypes.allTypes("ar", "ar") # siteLang, contentLang

# Get all categories in the database
all_categories = sdk.islamhouse.categoriesAndTypes.allCategories("ar")

# Complete category hierarchy tree
tree = sdk.islamhouse.categoriesAndTypes.categoriesTree("ar")

# Subcategories of a category with content lang localization
child_cats = sdk.islamhouse.categoriesAndTypes.childCategories(1, "ar", "ar") # categoryId, siteLang, contentLang

# Basic details of a category by ID
single_category = sdk.islamhouse.categoriesAndTypes.singleCategoryBasic(1, "ar")

# Subcategories with nested children
sub_categories = sdk.islamhouse.categoriesAndTypes.subCategories(1, "ar")

# Available material types under a specific category ID
category_types = sdk.islamhouse.categoriesAndTypes.categoryTypes(1, "ar", "ar")

# Available languages for materials within a category ID
category_langs = sdk.islamhouse.categoriesAndTypes.categoryLanguages(1, "ar", "ar") # id, slang, language

# ==========================================
# 2. Items Listings (items)
# ==========================================

# List materials by type (e.g. "books", "videos", "audios") and language
items = sdk.islamhouse.items.listItems("books", "ar", "ar", 1, 25) # type, siteLang, slang, page, limit

# List materials published by a specific author ID
author_items = sdk.islamhouse.items.authorItems(1, "ar", "ar", "ar", 1, 20) # authorId, slang, siteLang, contentLang, page, limit

# List materials categorized under a category ID
cat_items = sdk.islamhouse.items.categoryItems(1, "ar", "ar", "ar", 1, 20) # categoryId, slang, siteLang, contentLang, page, limit

# List latest items by period (e.g., "week", "month")
latest_items = sdk.islamhouse.items.latestItems("week", "ar", "ar", "ar", 1, 25) # period, slang, siteLang, contentLang, page, limit

# Highlighted featured items on the homepage
highlights = sdk.islamhouse.items.highlightedItems("ar", "ar") # siteLang, contentLang

# Get the total count of items available for a specific type
items_count = sdk.islamhouse.items.itemsCount("books", "ar", "ar") # type, siteLang, contentLang

# ==========================================
# 3. Single Item Details (item)
# ==========================================

# Details, metadata, and description of a single item
item_details = sdk.islamhouse.item.details(228065, "ar")

# List downloadable media/PDF attachments for an item
attachments = sdk.islamhouse.item.attachments(228065)

# Category tree path leading to this item
item_tree = sdk.islamhouse.item.tree(228065, "ar")

# Translation card details of the item
item_card_trans = sdk.islamhouse.item.cardTranslations(228065, "ar")

# Other translation languages available for this item
translations = sdk.islamhouse.item.translations(228065, "ar")

# ==========================================
# 4. Authors and Publishers (authors)
# ==========================================

# List authors/sources with filter and sort parameters
authors = sdk.islamhouse.authors.list({
    "kind": "author",     # Optional: "showall" | "author" | "source"
    "locale": "ar",       # Optional: "showall" | language code
    "sort": "countdesc",  # Optional
    "page": 1,            # Optional
    "perPage": 10         # Optional
})

# Specific author details by ID
author_details = sdk.islamhouse.authors.details(1, "ar")

# Translation card details of an author
author_card = sdk.islamhouse.authors.cardTranslations(1, "ar")

# Material types available for an author
author_types = sdk.islamhouse.authors.availableTypes(1, "ar", "ar")

# Languages available for an author
author_langs = sdk.islamhouse.authors.availableLocales(1, "ar", "ar")

# ==========================================
# 5. Languages & Terms (languages)
# ==========================================

# Details of all supported languages on the platform
lang_keys = sdk.islamhouse.languages.keys()

# Interface translation terms for localization
terms = sdk.islamhouse.languages.terms("ar")

# Available languages relative to another
avail_langs = sdk.islamhouse.languages.availableLanguages("ar", "ar")

# ==========================================
# 6. Holy Quran Recitations (quran)
# ==========================================

# Quran recitation categories (reciters, sections)
quran_categories = sdk.islamhouse.quran.categories("ar")

# Basic details of a Quran category
quran_category = sdk.islamhouse.quran.singleCategory(1, "ar")

# Details about a specific reciter
reciter_details = sdk.islamhouse.quran.authorDetails(1, "ar")

# Recitations list of a specific reciter
recitations = sdk.islamhouse.quran.authorRecitations(1, "ar")

# Detailed info of a specific Quran Surah
sura_details = sdk.islamhouse.quran.suraDetails(1, "ar")

# Audio recordings of a specific Surah by various reciters
sura_recitations = sdk.islamhouse.quran.suraRecitations(1, "ar")

# Details of a specific Quran recitation by ID
recitation = sdk.islamhouse.quran.recitationDetails(228065, "ar")
```

---

### Risalat Al-Haramain Source (Risalat Al-Haramain API)

**API Documentation Link:** [Risalat Al-Haramain API](https://risala.prh.gov.sa/en/Api/content)

```python
# ==========================================
# 1. Platform Contents (contents)
# ==========================================

# Get full content of the platform in a specific language
full_contents = sdk.risalatAlHaramain.contents.getFullContents({
    "language": "en", # Optional: URL language path (default: "en")
    "lang": "en"     # Optional: Query parameter language (default: "en")
})

# Retrieve contents with optional parameters
contents = sdk.risalatAlHaramain.contents.getContents({
    "language": "en",
    "lang": "en"
})

# Get detailed content of a single item
single_content = sdk.risalatAlHaramain.contents.singleContent(1, "en")

# Quick search items by name
name_search_result = sdk.risalatAlHaramain.contents.nameSearch("حصن", "ar")

# Check available translation languages for an item
risala_avail_langs = sdk.risalatAlHaramain.contents.availableLanguages(1, "ar")

# Get translation of a content item into a target language
content_translation = sdk.risalatAlHaramain.contents.contentTranslation(1, "en", "ar") # id, targetLanguage, language

# ==========================================
# 2. Islamic Content Modules (islamicContent)
# ==========================================

# Get Fatwas
fatwas = sdk.risalatAlHaramain.islamicContent.fatwas({
    "language": "en",    # Optional
    "lang": "ar",        # Optional
    "isFeatured": 1      # Optional: 0 or 1
})

# Get featured Hadiths
hadeeths = sdk.risalatAlHaramain.islamicContent.hadeeths({
    "language": "en",
    "lang": "ar",
    "isFeatured": 1
})

# Get featured Quran recitations
quran_content = sdk.risalatAlHaramain.islamicContent.quran({
    "language": "en",
    "lang": "ar",
    "isFeatured": 1
})

# ==========================================
# 3. Platform Search (search)
# ==========================================

# Keyword text search across platform content
search_result = sdk.risalatAlHaramain.search.contents("حصن", "en")

# ==========================================
# 4. Lookups & Meta (lookups)
# ==========================================

# Get available languages
risala_langs = sdk.risalatAlHaramain.lookups.languages("en")

# Get available content types
content_types = sdk.risalatAlHaramain.lookups.contentTypes("en")
```

---

### Bayan Al Islam Source (Bayan Al Islam API)

**Postman Resources:** [Collection](https://byenah.com/download-request?name=Bayan%20Al%20Islam.postman_collection.json) | [Environment](https://byenah.com/download-request?name=Bayan%20al%20islam%20env.postman_environment.json)

```python
# 1. Get list of available languages
bayan_langs = sdk.bayanAlIslam.languagesList("ar")

# 2. Get content list tailored for Muslims
muslim_list = sdk.bayanAlIslam.muslimList("en")

# 3. Get content list tailored for Non-Muslims
non_muslim_list = sdk.bayanAlIslam.nonMuslimList("en")

# 4. Get details of a specific content item by ID
content_details = sdk.bayanAlIslam.singleContent(22184, "en")

# 5. Get languages list paginated and filtered by name
paginated_langs = sdk.bayanAlIslam.paginatedLanguages({
    "name": "English", # Optional
    "page": 1,         # Optional
    "language": "en"   # Optional
})

# 6. Get recent contents (Muslim/Non-Muslim updates)
recent = sdk.bayanAlIslam.recentContents({
    "lang": "ar",
    "init": True,
    "ids": [22184], # Optional: content IDs list
    "language": "en" # Optional
})

# 7. Get website lookup variables
lookups = sdk.bayanAlIslam.lookups("en")

# 8. Search materials by title/name
search_result = sdk.bayanAlIslam.nameSearch("حصن", "ar")

# 9. Check available translation languages for a content ID
avail_langs = sdk.bayanAlIslam.availableLanguages(22184, "ar")

# 10. Get specific translation of a content item
translation = sdk.bayanAlIslam.contentTranslation(22184, "en", "ar") # id, targetLanguage, language

# 11. Get translations for media or PDF attachments of a content item
attachments_trans = sdk.bayanAlIslam.attachmentsTranslation(22184, "en", "ar") # id, targetLanguage, language
```

---

### Al Montaka Source (Al Montaka API)

**API Documentation Link:** [Al Montaka API](https://documenter.getpostman.com/view/5211979/2s8YzMZ6Fu)

```python
# ==========================================
# 1. Content and Comments (contents)
# ==========================================

# Get all comments for a specific content ID
comments = sdk.alMontaka.contents.comments(1)

# Add a new comment to a specific content item
new_comment = sdk.alMontaka.contents.addComment(1, "Test comment")

# Get filtered content by category IDs
filtered_content = sdk.alMontaka.contents.content([1, 2])

# ==========================================
# 2. Site Lookups and Filters (lookups)
# ==========================================

# Get target age groups
age_groups = sdk.alMontaka.lookups.ageGroups()

# Get categories matching language and name filter
categories = sdk.alMontaka.lookups.categories({
    "languageId": 1,
    "nameCont": "General"
})

# Get publishing entities matching language and name filter
entities = sdk.alMontaka.lookups.entities({
    "languageId": 1,
    "nameCont": "Dar"
})

# Get expertise/scientific levels matching filter
expert_levels = sdk.alMontaka.lookups.expertLevels({
    "languageId": 1,
    "nameCont": "Level"
})

# Get ideologies matching filter
ideologies = sdk.alMontaka.lookups.ideologies({
    "languageId": 1,
    "nameCont": "Sunnah",
    "parentId": 0
})

# Get available languages
languages = sdk.alMontaka.lookups.languages()

# Get/search scholars, narrators, or personalities
persons = sdk.alMontaka.lookups.persons({
    "nameCont": "Muhammad", # Optional
    "page": 1              # Optional
})

# Get website sections matching filter
sections = sdk.alMontaka.lookups.sections({
    "languageId": 1,
    "nameCont": "Section"
})

# Get tags matching filter
tags = sdk.alMontaka.lookups.tags({
    "languageId": 1,
    "nameCont": "Tag"
})

# Get targeted groups of audience
targeted_groups = sdk.alMontaka.lookups.targetedGroups()

# Get integrated YouTube channels list
youtube_channels = sdk.alMontaka.lookups.youtubeChannels()
```

---

## Donation & Support

You can support the projects and efforts of The Association for Multi-lingual Islamic Content through the following official channels:

- [Support Projects (Wakfy)](https://islamiccontent.org/Wakfy)
- [Bank Accounts](https://islamiccontent.org/Accounts)
- [Association Store](https://store.islamiccontent.sa/)
- [Annual Operational Support (الدعم التشغيلي السنوي للجمعية)](https://store.islamiccontent.sa/%D8%A7%D9%84%D9%85%D8%B5%D8%B1%D9%88%D9%81%D8%A7%D8%AA-%D8%A7%D9%84%D8%AA%D8%B4%D8%BA%D9%8A%D9%84%D9%8A%D8%A9-%D8%A7%D9%84%D8%B3%D9%86%D9%88%D9%8A%D8%A9-%D9%84%D9%84%D8%AC%D9%85%D8%B9%D9%8A-%D8%A9/p1950956689)
