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

yoruba_examples = [
    {
        'pattern': r'[aeiouẹọ]+',
        'description': 'Matches one or more Yoruba vowels (including open-mid vowels)',
        'test_words': ['aba', 'ọmọ', 'ẹja', 'ilé', 'consonant', 'ẹkọ'],
        'meaning': 'Pattern for vowel sequences in Yoruba'
    },
    {
        'pattern': r'[bdfghjklmnprstwybdfghjklmnprstwy]+[aeiouẹọ]+',
        'description': 'Consonant(s) followed by vowel(s) - basic Yoruba syllable structure',
        'test_words': ['ba', 'mọ', 'rẹ', 'gbọ', 'hello', 'kẹ'],
        'meaning': 'Basic CV (Consonant-Vowel) pattern'
    },
    {
        'pattern': r'(ọmọ|ilé|omi|ẹja|àgbà)',
        'description': 'Common Yoruba words pattern',
        'test_words': ['ọmọ', 'ilé', 'omi', 'ẹja', 'àgbà', 'house', 'other'],
        'meaning': 'Matches specific Yoruba words: ọmọ(child), ilé(house), omi(water), ẹja(fish), àgbà(elder)'
    },
    {
        'pattern': r'[aeiouẹọ]{2,3}',
        'description': 'Two to three consecutive vowels (vowel sequences in Yoruba)',
        'test_words': ['ìọ', 'ẹọ', 'aia', 'au', 'consonant', 'a'],
        'meaning': 'Vowel clusters of 2-3 vowels'
    },
    {
        'pattern': r'gb[aeiouẹọ]+[knm]?',
        'description': 'Words with gb digraph + vowels, optional final consonant',
        'test_words': ['gbọ', 'gba', 'gbẹ', 'hello', 'ba', 'gb'],
        'meaning': 'Yoruba words with gb digraph (labio-velar)'
    },
    {
        'pattern': r'[àáèéìíòóùúẹ̀ẹ́ọ̀ọ́]+[nlm]',
        'description': 'Tone-marked vowels followed by nasal/liquid consonants',
        'test_words': ['àn', 'ọ́n', 'ẹ́l', 'hello', 'an', 'ọn'],
        'meaning': 'Tonal vowel + nasal/liquid ending pattern'
    },
    {
        'pattern': r'[kp][aeiouẹọ]+[kp]',
        'description': 'Labio-velar consonants (kp) pattern',
        'test_words': ['kpọ', 'kpa', 'kpẹ', 'hello', 'ka', 'pa'],
        'meaning': 'Words with labio-velar kp sound'
    },
    {
        'pattern': r'[yw][aeiouẹọ]+',
        'description': 'Semi-vowel initial pattern (y/w + vowel)',
        'test_words': ['yẹ', 'wọ', 'ya', 'wi', 'hello', 'ba'],
        'meaning': 'Words starting with semi-vowels y or w'
    },
    {
        'pattern': r'(ní|sí|tí|kí)',
        'description': 'Common Yoruba function words with high tone',
        'test_words': ['ní', 'sí', 'tí', 'kí', 'hello', 'na'],
        'meaning': 'High-tone function words: ní(in/at), sí(to), tí(that), kí(what)'
    },
    {
        'pattern': r'[òọ̀àèì][a-z]+[ẹọ]$',
        'description': 'Low-tone initial vowel + consonant(s) + final mid vowel',
        'test_words': ['òkẹ', 'àgbọ', 'ìbẹ', 'hello', 'age', 'oke'],
        'meaning': 'Low tone initial pattern common in Yoruba nouns'
    }
]