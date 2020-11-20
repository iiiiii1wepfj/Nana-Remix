import yaml
from codecs import encode, decode

from nana import logging as LOGGER
from nana.modules.database.lang_db import prev_locale
from nana import Owner

LANGUAGES = ['en-US', 'hi', 'he', 'id', 'fa']

strings = {
    i: yaml.full_load(open("locales/" + i + ".yml", "r")) for i in LANGUAGES
}


def tld(t, _show_none=True):
    LANGUAGE = prev_locale(Owner)

    if LANGUAGE:
        LOCALE = LANGUAGE.locale_name
        if LOCALE in ('en-US') and t in strings['en-US']:
            result = decode(
                encode(strings['en-US'][t], 'latin-1', 'backslashreplace'),
                'unicode-escape')
            return result
        elif LOCALE in ('hi') and t in strings['hi']:
            result = decode(
                encode(strings['hi'][t], 'latin-1', 'backslashreplace'),
                'unicode-escape')
            return result
        elif LOCALE in ('he') and t in strings['he']:
            result = decode(
                encode(strings['he'][t], 'latin-1', 'backslashreplace'),
                'unicode-escape')
            return result
        elif LOCALE in ('id') and t in strings['id']:
            result = decode(
                encode(strings['id'][t], 'latin-1', 'backslashreplace'),
                'unicode-escape')
            return result
        elif LOCALE in ('fa') and t in strings['fa']:
            result = decode(
                encode(strings['fa'][t], 'latin-1', 'backslashreplace'),
                'unicode-escape')
            return result

    if t in strings['en-US']:
        result = decode(
            encode(strings['en-US'][t], 'latin-1', 'backslashreplace'),
            'unicode-escape')
        return result

    err = f"No string found for {t}.\nReport it in @nanabotsupport."
    LOGGER.warning(err)
    return err


def tld_list(t):
    LANGUAGE = prev_locale(Owner)

    if LANGUAGE:
        LOCALE = LANGUAGE.locale_name
        if LOCALE in ('en-US') and t in strings['en-US']:
            return strings['en-US'][t]
        elif LOCALE in ('hi') and t in strings['hi']:
            return strings['hi'][t]
        elif LOCALE in ('he') and t in strings['he']:
            return strings['he'][t]
        elif LOCALE in ('id') and t in strings['id']:
            return strings['id'][t]
        elif LOCALE in ('fa') and t in strings['fa']:
            return strings['id'][t]

    if t in strings['en-US']:
        return strings['en-US'][t]

    LOGGER.warning(f"#NOSTR No string found for {t}.")
    return f"No string found for {t}.\nReport it in @nanabotsupport."