#!/usr/bin/env python3

import unicodedata
from emot.emo_unicode import UNICODE_EMOJI as EMOJIS
from .emotions_char import EMOTICONS_EXPAND as EMOTICONS
from .emotions_char import DONGER_EMO as DONGERS

__all__ = ["convert_accents", "convert_dongers", "convert_emojis", "convert_emoticons"]

def convert_accents(text):
    return ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))

def convert_dongers(text):
    for donger in DONGERS:
        text = text.replace(donger, "_".join(DONGERS[donger].replace(",","").replace(":","").split()))
    return text

def convert_emojis(text):
    for emoj in EMOJIS:
        text = text.replace(emoj, "_".join(EMOJIS[emoj].replace(",","").replace(":","").split()))
    return text

def convert_emoticons(text):
    for emot in EMOTICONS:
        text = text.replace(emot, "_".join(EMOTICONS[emot].replace(",","").replace(":","").split()))
    return text
