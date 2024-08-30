import requests


YANDEX_SPELLER_URL = "https://speller.yandex.net/services/spellservice.json/checkText"


def check_spelling(text: str) -> list:
    response = requests.get(YANDEX_SPELLER_URL, params={"text": text})
    result = response.json()
    if result:
        return [error["word"] for error in result]
    return []
