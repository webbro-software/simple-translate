import pytest
from simple_translate import EasyTranslate

translator = EasyTranslate()

def test_translation_uz_to_en():
    translated_text = translator.translate("salom", "en", "uz")
    assert translated_text == "hello"

def test_translation_en_to_uz():
    translated_text = translator.translate("how are you", "uz", "en")
    assert translated_text == "qalaysiz"

def test_translation_en_to_fr():
    translated_text = translator.translate("apple", "fr", "en")
    assert translated_text == "pomme"

def test_translation_en_to_kr():
    translated_text = translator.translate("apple", "ko", "en")
    assert translated_text == "사과"
