# -*- coding: utf-8 -*-


'''
How Secure is My Password? Python Module
'''


import math
import re


class Character():
    '''
    Character module will be help to know the possibility combinations

    Parameters
    ----------
    password : str
        the string contains the password value.

    Attributes
    ----------
    contained_in_sets : list
        List of char type is been used
    possible_characters : int/float
        Number os possible characters combination.
    character_sets_dictionary : dict
        Configuration of test char
    '''

    def __init__(self, password):
        if not isinstance(password, str):
            raise Exception('password is an invalid type', password)

        self.contained_in_sets = []
        self.possible_characters = 0
        self.character_sets_dictionary = {
            "ASCII Control Character": ["[\\u0000-\\u001F]", 32],
            "ASCII Lowercase": ["[a-z]", 26],
            "ASCII Uppercase": ["[A-Z]", 26],
            "ASCII Numbers": ["\\d", 10],
            "ASCII Top Row Symbols": ["[-!@£#$%^&*()=+_]", 15],
            "ASCII Other Symbols": ["[\\s\\?\\/\\.>,<`~\\|;:\\]}\\[{'\"\\\\]", 19],
            "Unicode Latin 1 Supplement": ["[\\u00A1-\\u00A2\\u00A4-\\u00FF]", 93],
            "Unicode Latin 1 Supplement Non Standard": ["[\\u0080-\\u00A0]", 33],
            "Unicode Latin Extended A": ["[\\u0100-\\u017F]", 128],
            "Unicode Latin Extended B": ["[\\u0180-\\u024F]", 208],
            "Unicode Latin Extended C": ["[\\u2C60-\\u2C7F]", 32],
            "Unicode Latin Extended D": ["[\\uA720-\\uA7FF]", 29],
            "Unicode Cyrillic Uppercase": ["[\\u0410-\\u042F]", 32],
            "Unicode Cyrillic Lowercase": ["[\\u0430-\\u044F]", 32]
        }

        for item in self.character_sets_dictionary.items():
            key = item[0]
            value = self.character_sets_dictionary[key]
            re_value = value[0]
            possibility = value[1]

            length = len(password)
            password = re.sub(r'%s' % re_value, '', password)

            if not length == len(password):
                self.contained_in_sets.append(key)
                self.possible_characters += possibility

        if len(password) > 0:
            self.contained_in_sets.append('Unspecified Unicode')
            self.possible_characters += 1e3


class Hsimpy():
    '''
    Rather than just saying a password is "weak" or "strong",
    *How Secure is My Password?* lets your users know how long it would
    take someone to crack their password.

    Parameters
    ----------
    password : str
        the string contains the password value.

    Attributes
    ----------
    conf : dict
        COnfiguration using to calc the strength
    possible_characters : int
        Number os possible character.
    possible_combinations : int/float
        Number os possible characters combination.
    time_in_seconds : int/float
        Time to broke passwork using 10bilions operation p/s
    security_level : str
        bad, ok, good
    '''

    def __init__(self, password):
        # import pdb; pdb.set_trace()
        if not isinstance(password, str):
            raise TypeError('password is an invalid type', password)

        self.conf = {
            "calculations_per_second": 3900000,  # 1e10 10 billion
            "good": 31557600e3,  # 31557600e6 1 million years
            "ok": 31557600e1  # 31557600 1 year
        }

        char = Character(password)

        self.possible_characters = char.possible_characters
        self.possible_combinations = math.pow(self.possible_characters, len(password))
        self.time_in_seconds = self.possible_combinations / self.conf['calculations_per_second']
        self.security_level = 'bad'

        if self.time_in_seconds >= self.conf['good']:
            self.security_level = 'good'
        elif self.time_in_seconds >= self.conf['ok']:
            self.security_level = 'ok'
