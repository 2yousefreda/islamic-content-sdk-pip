# Islamic Content SDK (Python)

An integrated and easy-to-use software library for Python developers to fetch authentic Islamic content (The Holy Qur'an and Hadith) in multiple languages directly from official sources.

This project is developed for [The Association for Multi-lingual Islamic Content](https://islamiccontent.sa/).

> [!TIP]
> **AI & LLM Integration**: You can also use the official [Model Context Protocol (MCP) Server](https://www.npmjs.com/package/islamic-content-mcp-server) to connect this SDK directly to AI assistants like Claude Desktop, Cursor, VS Code, and more.

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

Below is a complete guide on how to interact with every single method available in the SDK, including the exact API endpoints and JSON response structures.

### Quran Source (QuranEnc API)

**API Documentation Link:** [QuranEnc API](https://quranenc.com/en/home/api/)

```python
# 1. Get available translations list on the platform
# HTTP Endpoint: GET https://quranenc.com/api/v1/translations/list/{language}?localization={localization}
# Response Shape:
# [
#   {
#     "translation_number": 1,
#     "language_code": "es",
#     "language_name": "Español",
#     "translation_name": "...",
#     "translation_key": "..."
#   }
# ]
translations = sdk.quranenc.translationList({
    "language": "es",      # Optional: Filter list by language code
    "localization": "ar"   # Optional: Localize names in the response
})

# 2. Translate an entire sura (Al-Fatiha in Spanish)
# HTTP Endpoint: GET https://quranenc.com/api/v1/translation/sura/{translationKey}/{suraNumber}
# Response Shape:
# {
#   "result": [
#     {
#       "id": "1",
#       "sura": "1",
#       "aya": "1",
#       "translation": "En el nombre de Alá, el Compasivo, el Misericordioso.",
#       "footnotes": ""
#     }
#   ]
# }
sura = sdk.quranenc.translationSura("spanish_montada_eu", 1)

# 3. Translate a specific verse (Ayah 1 of Sura 1)
# HTTP Endpoint: GET https://quranenc.com/api/v1/translation/aya/{translationKey}/{suraNumber}/{ayaNumber}
# Response Shape:
# {
#   "result": {
#     "id": "1",
#     "sura": "1",
#     "aya": "1",
#     "translation": "En el nombre de Alá, el Compasivo, el Misericordioso.",
#     "footnotes": ""
#   }
# }
aya = sdk.quranenc.translationAya("spanish_montada_eu", 1, 1)

# 4. Get the audio MP3 file details for a specific verse
# HTTP Endpoint: GET https://d.quranenc.com/data/audio/{translationKey}/{sura3Digits}{aya3Digits}.mp3
# Response Shape:
# {
#   "status": 200,
#   "file_url": "https://d.quranenc.com/data/audio/chinese_suliman/001001.mp3",
#   "content_type": "audio/mpeg"
# }
audio = sdk.quranenc.ayaAudio("chinese_suliman", 1, 1)

# 5. Submit translation feedback/note (POST request)
# HTTP Endpoint: POST https://quranenc.com/api/v1/translations/note
# Response Shape:
# {
#   "message": "Note added successfully"
# }
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
# HTTP Endpoint: GET https://hadeethenc.com/api/v1/languages
# Response Shape:
# [
#   {
#     "code": "ar",
#     "native": "العربية"
#   }
# ]
languages = sdk.hadeethenc.languages()

# 2. Get categories of Hadith translated in a specific language (supports local filtering by parent_id)
# HTTP Endpoint: GET https://hadeethenc.com/api/v1/categories/list/?language={languageCode}
# Response Shape:
# [
#   {
#     "id": "1",
#     "title": "Belief",
#     "parent_id": None
#   }
# ]
categories = sdk.hadeethenc.categories("en", 1) # Optional: parent_id to filter subcategories locally

# 3. Get main (root) categories of Hadith in English
# HTTP Endpoint: GET https://hadeethenc.com/api/v1/categories/roots/?language={languageCode}
# Response Shape:
# [
#   {
#     "id": "1",
#     "title": "Belief",
#     "parent_id": None
#   }
# ]
root_categories = sdk.hadeethenc.rootCategories("en")

# 4. List Hadiths under a category with pagination
# HTTP Endpoint: GET https://hadeethenc.com/api/v1/hadeeths/list/?language={language}&category_id={categoryId}&page={page}&per_page={perPage}
# Response Shape:
# [
#   {
#     "id": "2962",
#     "title": "...",
#     "category_id": "1"
#   }
# ]
hadiths = sdk.hadeethenc.hadithsList({
    "language": "en",
    "categoryId": 1,  # Optional
    "page": 1,        # Optional
    "perPage": 20     # Optional
})

# 5. Get full explanation, translations, and grade of a specific Hadith by ID
# HTTP Endpoint: GET https://hadeethenc.com/api/v1/hadeeths/one/?id={id}&language={language}
# Response Shape:
# {
#   "id": "2962",
#   "title": "...",
#   "hadeeth": "...",
#   "attribution": "...",
#   "grade": "Authentic",
#   "explanation": "..."
# }
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
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/sitecontent/{siteLang}/{contentLang}/json
# Response Shape: [ { "block_name": "showall", "type": "section", "items_count": 12648, "api_url": "..." } ]
types = sdk.islamhouse.categoriesAndTypes.allTypes("ar", "ar") # siteLang, contentLang

# Get all categories in the database
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/categories/showall/{language}/json
# Response Shape: [ { "id": 1, "title": "...", "description": "..." } ]
all_categories = sdk.islamhouse.categoriesAndTypes.allCategories("ar")

# Complete category hierarchy tree
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-object-category-tree/{language}/json
# Response Shape: [ { "id": 1, "name": "...", "children": [...] } ]
tree = sdk.islamhouse.categoriesAndTypes.categoriesTree("ar")

# Subcategories of a category with content lang localization
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/categories/viewcat/{categoryId}/{siteLang}/{contentLang}/json
# Response Shape: [ { "id": 1, "title": "..." } ]
child_cats = sdk.islamhouse.categoriesAndTypes.childCategories(1, "ar", "ar") # categoryId, siteLang, contentLang

# Basic details of a category by ID
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/categories/viewitem/{categoryId}/{language}/json
# Response Shape: { "id": 1, "title": "..." }
single_category = sdk.islamhouse.categoriesAndTypes.singleCategoryBasic(1, "ar")

# Subcategories with nested children
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-sub-categories/{categoryId}/{language}/json
# Response Shape: [ { "id": 1, "title": "..." } ]
sub_categories = sdk.islamhouse.categoriesAndTypes.subCategories(1, "ar")

# Available material types under a specific category ID
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-category-types-available/{categoryId}/{siteLang}/{contentLang}/json
# Response Shape: [ { "type": "books", "count": 5 } ]
category_types = sdk.islamhouse.categoriesAndTypes.categoryTypes(1, "ar", "ar")

# Available languages for materials within a category ID
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-category-source-languages/{categoryId}/{slang}/{language}/json
# Response Shape: [ { "code": "ar", "name": "Arabic" } ]
category_langs = sdk.islamhouse.categoriesAndTypes.categoryLanguages(1, "ar", "ar") # id, slang, language

# ==========================================
# 2. Items Listings (items)
# ==========================================

# List materials by type (e.g. "books", "videos", "audios") and language
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/{type}/{siteLang}/{slang}/{page}/{limit}/json
# Response Shape: [ { "id": 1, "title": "...", "type": "books" } ]
items = sdk.islamhouse.items.listItems("books", "ar", "ar", 1, 25) # type, siteLang, slang, page, limit

# List materials published by a specific author ID
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-author-items/{authorId}/{slang}/{siteLang}/{contentLang}/{page}/{limit}/json
# Response Shape: [ { "id": 1, "title": "..." } ]
author_items = sdk.islamhouse.items.authorItems(1, "ar", "ar", "ar", 1, 20) # authorId, slang, siteLang, contentLang, page, limit

# List materials categorized under a category ID
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-category-items/{categoryId}/{slang}/{siteLang}/{contentLang}/{page}/{limit}/json
# Response Shape: [ { "id": 1, "title": "..." } ]
cat_items = sdk.islamhouse.items.categoryItems(1, "ar", "ar", "ar", 1, 20) # categoryId, slang, siteLang, contentLang, page, limit

# List latest items by period (e.g., "week", "month")
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-latest/{period}/{slang}/{siteLang}/{contentLang}/{page}/{limit}/json
# Response Shape: [ { "id": 1, "title": "..." } ]
latest_items = sdk.islamhouse.items.latestItems("week", "ar", "ar", "ar", 1, 25) # period, slang, siteLang, contentLang, page, limit

# Highlighted featured items on the homepage
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-highlights/{siteLang}/{contentLang}/json
# Response Shape: [ { "id": 1, "title": "..." } ]
highlights = sdk.islamhouse.items.highlightedItems("ar", "ar") # siteLang, contentLang

# Get the total count of items available for a specific type
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-language-items-count/{type}/{siteLang}/{contentLang}/json
# Response Shape: { "count": 100 }
items_count = sdk.islamhouse.items.itemsCount("books", "ar", "ar") # type, siteLang, contentLang

# ==========================================
# 3. Single Item Details (item)
# ==========================================

# Details, metadata, and description of a single item
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-item/{itemId}/{language}/json
# Response Shape: { "id": 228065, "title": "...", "description": "...", "prepared_by": [...] }
item_details = sdk.islamhouse.item.details(228065, "ar")

# List downloadable media/PDF attachments for an item
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/check-attachment/{itemId}/json
# Response Shape: [ { "id": 1, "file_url": "...", "size": "..." } ]
attachments = sdk.islamhouse.item.attachments(228065)

# Category tree path leading to this item
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-item-tree/{itemId}/{language}/json
# Response Shape: [ { "id": 1, "name": "..." } ]
item_tree = sdk.islamhouse.item.tree(228065, "ar")

# Translation card details of the item
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-item-card-translations/{itemId}/{language}/json
# Response Shape: { "title": "...", "description": "..." }
item_card_trans = sdk.islamhouse.item.cardTranslations(228065, "ar")

# Other translation languages available for this item
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-item-translations/{itemId}/{language}/json
# Response Shape: [ { "locale": "en", "title": "..." } ]
translations = sdk.islamhouse.item.translations(228065, "ar")

# ==========================================
# 4. Authors (authors)
# ==========================================

# List authors/sources (عرض المؤلفين/المصادر)
# params: kind, locale, sort, page, perPage
authors_list = sdk.islamhouse.authors.list({"kind": "showall", "locale": "ar", "page": 1})

# Specific author details by ID
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-author/{authorId}/{language}/json
# Response Shape: { "id": 1, "name": "...", "description": "..." }
author_details = sdk.islamhouse.authors.details(1, "ar")

# Translation card details of an author
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-author-card-translations/{authorId}/{language}/json
# Response Shape: { "name": "...", "description": "..." }
author_card = sdk.islamhouse.authors.cardTranslations(1, "ar")

# Material types available for an author
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-author-types-avaliable/{authorId}/{siteLang}/{contentLang}/json
# Response Shape: [ { "type": "books", "count": 5 } ]
author_types = sdk.islamhouse.authors.availableTypes(1, "ar", "ar")

# Languages available for an author
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-author-available-languages/{authorId}/{slang}/{language}/json
# Response Shape: [ { "code": "ar", "name": "Arabic" } ]
author_langs = sdk.islamhouse.authors.availableLocales(1, "ar", "ar")

# ==========================================
# 5. Languages & Terms (languages)
# ==========================================

# Details of all supported languages on the platform
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/languages/get-language-details/json
# Response Shape: [ { "code": "ar", "name": "Arabic" } ]
lang_keys = sdk.islamhouse.languages.keys()

# Interface translation terms for localization
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/languages/get-language-terms/{language}/json
# Response Shape: { "term_key": "term_value" }
terms = sdk.islamhouse.languages.terms("ar")

# Available languages relative to another
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/main/get-available-languages/{slang}/{language}/json
# Response Shape: [ { "code": "ar", "name": "Arabic" } ]
avail_langs = sdk.islamhouse.languages.availableLanguages("ar", "ar")

# ==========================================
# 6. Holy Quran Recitations (quran)
# ==========================================

# Quran recitation categories (reciters, sections)
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/quran/get-categories/{language}/json
# Response Shape: [ { "id": 1, "name": "..." } ]
quran_categories = sdk.islamhouse.quran.categories("ar")

# Basic details of a Quran category
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/quran/get-category/{categoryId}/{language}/json
# Response Shape: { "id": 1, "name": "..." }
quran_category = sdk.islamhouse.quran.singleCategory(1, "ar")

# Details about a specific reciter
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/quran/get-author/{reciterId}/{language}/json
# Response Shape: { "id": 1, "name": "..." }
reciter_details = sdk.islamhouse.quran.authorDetails(1, "ar")

# Recitations list of a specific reciter
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/quran/get-author-recitations/{reciterId}/{language}/json
# Response Shape: [ { "id": 1, "title": "..." } ]
recitations = sdk.islamhouse.quran.authorRecitations(1, "ar")


# Audio recordings of a specific Surah by various reciters
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/quran/get-sura-recitations/{suraId}/{language}/json
# Response Shape: [ { "id": 1, "title": "..." } ]
sura_recitations = sdk.islamhouse.quran.suraRecitations(1, "ar")

# Details of a specific Quran recitation by ID
# HTTP Endpoint: GET https://api3.islamhouse.com/v3/paV29H2gm56kvLPy/quran/get-recitation/{recitationId}/{language}/json
# Response Shape: { "id": 228065, "title": "...", "audio_url": "..." }
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
# HTTP Endpoint: GET https://risala.prh.gov.sa/{language}/Api/get_full_contents?lang={lang}
# Response Shape: { "data": [ { "id": 81, "name": "...", "description": "..." } ] }
full_contents = sdk.risalatAlHaramain.contents.getFullContents({
    "language": "en", # Optional: URL language path (default: "en")
    "lang": "en"     # Optional: Query parameter language (default: "en")
})

# Retrieve contents with optional parameters
# HTTP Endpoint: GET https://risala.prh.gov.sa/{language}/Api/content?lang={lang}
# Response Shape: { "data": [ { "id": 81, "name": "..." } ] }
contents = sdk.risalatAlHaramain.contents.getContents({
    "language": "en",
    "lang": "en"
})

# Get detailed content of a single item
# HTTP Endpoint: GET https://risala.prh.gov.sa/{language}/Api/single-content?id={contentId}
# Response Shape: { "data": { "id": 1, "name": "..." } }
single_content = sdk.risalatAlHaramain.contents.singleContent(1, "en")





# ==========================================
# 2. Islamic Content Modules (islamicContent)
# ==========================================

# Get Fatwas
# HTTP Endpoint: GET https://risala.prh.gov.sa/{language}/Api/fatwas?lang={lang}&is_featured={isFeatured}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
fatwas = sdk.risalatAlHaramain.islamicContent.fatwas({
    "language": "en",    # Optional
    "lang": "ar",        # Optional
    "isFeatured": 1      # Optional: 0 or 1
})

# Get featured Hadiths
# HTTP Endpoint: GET https://risala.prh.gov.sa/{language}/Api/hadeeths?lang={lang}&is_featured={isFeatured}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
hadeeths = sdk.risalatAlHaramain.islamicContent.hadeeths({
    "language": "en",
    "lang": "ar",
    "isFeatured": 1
})

# Get featured Quran recitations
# HTTP Endpoint: GET https://risala.prh.gov.sa/{language}/Api/quran?lang={lang}&is_featured={isFeatured}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
quran_content = sdk.risalatAlHaramain.islamicContent.quran({
    "language": "en",
    "lang": "ar",
    "isFeatured": 1
})

# ==========================================
# 3. Platform Search (search)
# ==========================================

# Keyword text search across platform content
# HTTP Endpoint: GET https://risala.prh.gov.sa/{language}/Api/search?query={query}&page={page}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ], "meta": { "current_page": 1, "total": 1232 } }
search_result = sdk.risalatAlHaramain.search.contents("حصن", "en", 1) # Optional: page number

# ==========================================
# 4. Lookups & Meta (lookups)
# ==========================================

# Get available languages
# HTTP Endpoint: GET https://risala.prh.gov.sa/{language}/Api/langs?api_key={apiKey}
# Response Shape: { "data": [ { "id": 51, "iso_code": "en", "name": "English" } ] }
risala_langs = sdk.risalatAlHaramain.lookups.languages("en")

# Get available content types
# HTTP Endpoint: GET https://risala.prh.gov.sa/{language}/Api/content-types
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
content_types = sdk.risalatAlHaramain.lookups.contentTypes("en")
```

---

### Bayan Al Islam Source (Bayan Al Islam API)

**Postman Resources:** [Collection](https://byenah.com/download-request?name=Bayan%20Al%20Islam.postman_collection.json) | [Environment](https://byenah.com/download-request?name=Bayan%20al%20islam%20env.postman_environment.json)

```python
# 1. Get list of available languages
# HTTP Endpoint: GET https://byenah.com/{language}/Api/languages/list
# Response Shape: { "data": [ { "id": 51, "name_en": "English", "iso_code": "en" } ] }
bayan_langs = sdk.bayanAlIslam.languagesList("ar")

# 2. Get content list tailored for Muslims
# HTTP Endpoint: GET https://byenah.com/{language}/Api/content/muslims/full_list?page={page}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ], "meta": { "current_page": 1, "total": 50 } }
muslim_list = sdk.bayanAlIslam.muslimList("en", 1) # Optional: page number

# 3. Get content list tailored for Non-Muslims
# HTTP Endpoint: GET https://byenah.com/{language}/Api/content/non-muslims/full_list?page={page}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ], "meta": { "current_page": 1, "total": 50 } }
non_muslim_list = sdk.bayanAlIslam.nonMuslimList("en", 1) # Optional: page number


# 5. Get languages list paginated and filtered by name
# HTTP Endpoint: GET https://byenah.com/{language}/Api/paginated-languages?name={name}&page={page}
# Response Shape: { "data": [ { "id": 51, "name": "..." } ] }
paginated_langs = sdk.bayanAlIslam.paginatedLanguages({
    "name": "English", # Optional
    "page": 1,         # Optional
    "language": "en"   # Optional
})

# 6. Get recent contents (Muslim/Non-Muslim updates)
# HTTP Endpoint: GET https://byenah.com/{language}/Api/recent-contents?lang={lang}&init={init}&ids={ids}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
recent = sdk.bayanAlIslam.recentContents({
    "lang": "ar",
    "init": True,
    "ids": [22184], # Optional: content IDs list
    "language": "en" # Optional
})

# 7. Get website lookup variables
# HTTP Endpoint: GET https://byenah.com/{language}/Api/lookups
# Response Shape: { "data": { "categories": [...] } }
lookups = sdk.bayanAlIslam.lookups("en")

# 8. Search materials by title/name
# HTTP Endpoint: GET https://byenah.com/{language}/Api/name_search?name={name}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
search_result = sdk.bayanAlIslam.nameSearch("حصن", "ar")


```

---

### Al Montaka Source (Al Montaka API)

**API Documentation Link:** [Al Montaka API](https://documenter.getpostman.com/view/5211979/2s8YzMZ6Fu)

```python
# ==========================================
# 1. Content and Comments (contents)
# ==========================================

# Get all latest contents with pagination
# HTTP Endpoint: GET https://content.mofeed.org/Api/content?page={page}
# Response Shape: { "data": { "current_page": 1, "data": [ { "id": 1, "title": "..." } ] }, "meta": { "total": 5958 } }
contents_list = sdk.alMontaka.contents.list(1) # Optional: page number, Optional: categories[]

# Get all comments for a specific content ID
# HTTP Endpoint: GET https://content.mofeed.org/Api/comments?content_id={contentId}
# Response Shape: { "message": "", "errors": [], "data": { "current_page": 1, "data": [ { "id": 10702, "comment": "..." } ] } }
comments = sdk.alMontaka.contents.comments(1)

# Add a new comment to a specific content item
# HTTP Endpoint: POST https://content.mofeed.org/Api/comment
# Request Body: content_id={contentId}&comment={comment}
# Response Shape: { "message": "Comment added successfully" }
new_comment = sdk.alMontaka.contents.addComment(1, "Test comment")


# ==========================================
# 2. Site Lookups and Filters (lookups)
# ==========================================

# Get target age groups
# HTTP Endpoint: GET https://content.mofeed.org/Api/age-groups
# Response Shape: { "message": "", "errors": [], "data": [ { "id": 1, "name": "From 18 to 25" } ] }
age_groups = sdk.alMontaka.lookups.ageGroups()

# Get categories matching language and name filter
# HTTP Endpoint: GET https://content.mofeed.org/Api/categories?language_id={languageId}&name_cont={nameCont}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
categories = sdk.alMontaka.lookups.categories({
    "languageId": 1,
    "nameCont": "General"
})

# Get publishing entities matching language and name filter
# HTTP Endpoint: GET https://content.mofeed.org/Api/entities?language_id={languageId}&name_cont={nameCont}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
entities = sdk.alMontaka.lookups.entities({
    "languageId": 1,
    "nameCont": "Dar"
})

# Get expertise/scientific levels matching filter
# HTTP Endpoint: GET https://content.mofeed.org/Api/expert-levels?language_id={languageId}&name_cont={nameCont}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
expert_levels = sdk.alMontaka.lookups.expertLevels({
    "languageId": 1,
    "nameCont": "Level"
})

# Get ideologies matching filter
# HTTP Endpoint: GET https://content.mofeed.org/Api/ideologies?language_id={languageId}&name_cont={nameCont}&parent_id={parentId}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
ideologies = sdk.alMontaka.lookups.ideologies({
    "languageId": 1,
    "nameCont": "Sunnah",
    "parentId": 0
})

# Get available languages
# HTTP Endpoint: GET https://content.mofeed.org/Api/languages
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
languages = sdk.alMontaka.lookups.languages()

# Get/search scholars, narrators, or personalities
# HTTP Endpoint: GET https://content.mofeed.org/Api/persons?name_cont={nameCont}&page={page}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
persons = sdk.alMontaka.lookups.persons({
    "nameCont": "Muhammad", # Optional
    "page": 1              # Optional
})

# Get website sections matching filter
# HTTP Endpoint: GET https://content.mofeed.org/Api/sections?language_id={languageId}&name_cont={nameCont}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
sections = sdk.alMontaka.lookups.sections({
    "languageId": 1,
    "nameCont": "Section"
})

# Get tags matching filter
# HTTP Endpoint: GET https://content.mofeed.org/Api/tags?language_id={languageId}&name_cont={nameCont}
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
tags = sdk.alMontaka.lookups.tags({
    "languageId": 1,
    "nameCont": "Tag"
})

# Get targeted groups of audience
# HTTP Endpoint: GET https://content.mofeed.org/Api/targeted-groups
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
targeted_groups = sdk.alMontaka.lookups.targetedGroups()

# Get integrated YouTube channels list
# HTTP Endpoint: GET https://content.mofeed.org/Api/youtube-channels
# Response Shape: { "data": [ { "id": 1, "name": "..." } ] }
youtube_channels = sdk.alMontaka.lookups.youtubeChannels()
```

---

## Donation & Support

You can support the projects and efforts of The Association for Multi-lingual Islamic Content through the following official channels:

- [Support Projects (Wakfy)](https://islamiccontent.org/Wakfy)
- [Bank Accounts](https://islamiccontent.org/Accounts)
- [Association Store](https://store.islamiccontent.sa/)
- [Annual Operational Support (الدعم التشغيلي السنوي للجمعية)](https://store.islamiccontent.sa/%D8%A7%D9%84%D9%85%D8%B5%D8%B1%D9%88%D9%81%D8%A7%D8%AA-%D8%A7%D9%84%D8%AA%D8%B4%D8%BA%D9%8A%D9%84%D9%8A%D8%A9-%D8%A7%D9%84%D8%B3%D9%86%D9%88%D9%8A%D8%A9-%D9%84%D9%84%D8%AC%D9%85%D8%B9%D9%8A-%D8%A9/p1950956689)
