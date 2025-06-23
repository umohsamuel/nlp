efik_examples = [
    {
        'pattern': r'[aeiọụẹị]+',
        'description': 'Matches one or more Efik vowels (including tone-marked vowels)',
        'test_words': ['aba', 'ọkọ', 'ịdịa', 'mme', 'consonant', 'ẹkẹ'],
        'meaning': 'Pattern for vowel sequences in Efik'
    },
    {
        'pattern': r'[kmnñpst]+[aeiọụẹị]+',
        'description': 'Consonant(s) followed by vowel(s) - basic Efik syllable structure',
        'test_words': ['ka', 'mme', 'nta', 'ñko', 'hello', 'sta'],
        'meaning': 'Consonant-Vowel pattern'
    },
    {
        'pattern': r'(mme|eka|oro|ado)',
        'description': 'Common Efik words pattern',
        'test_words': ['mme', 'eka', 'oro', 'ado', 'house', 'other'],
        'meaning': 'Matches specific Efik words: mme(water), eka(one), oro(word), ado(place)'
    },
    {
        'pattern': r'[aeiọụẹị]{2,3}',
        'description': 'Two to three consecutive vowels (common in Efik)',
        'test_words': ['ịọ', 'ọọọ', 'eia', 'ai', 'consonant', 'a'],
        'meaning': 'Vowel clusters of 2-3 vowels'
    },
    {
        'pattern': r'ñ[aeiọụẹị]+[kpt]?',
        'description': 'Words starting with ñ (palatalized n) + vowels, optional final consonant',
        'test_words': ['ñak', 'ñia', 'ñọ', 'hello', 'mak', 'ñ'],
        'meaning': 'Efik words with palatalized n'
    },
    {
        'pattern': r'[ụụọọẹẹịị]+[bmn]',
        'description': 'Tone-marked vowels followed by nasal consonants',
        'test_words': ['ụọm', 'ẹẹn', 'ịịb', 'hello', 'an', 'ọn'],
        'meaning': 'Tonal vowel + nasal ending pattern'
    }
]