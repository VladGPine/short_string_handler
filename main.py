import unittest


def short_title_handler(text: str) -> str:
    try:
        result_string = None
        all_words_in_text = text.split()
        length_checker = 25
        if len(text) > length_checker:
            raw_string = ''
            for each_word in all_words_in_text:
                if len(all_words_in_text[0] + '...') > length_checker:
                    result_string = all_words_in_text[0][:22] + '...'
                elif len(raw_string + each_word + '...') > length_checker:
                    break
                else:
                    raw_string += each_word + ' '
                    result_string = f'{raw_string.strip()}...'
        elif len(text) == 0:
            return ''
        else:
            result_string = text
    except AttributeError:
        return 'Not a string!'
    else:
        return result_string


class StringTests(unittest.TestCase):

    def test_not_a_string(self):
        self.assertEqual(short_title_handler(1), 'Not a string!')

    def test_empty_string(self):
        self.assertEqual(short_title_handler(''), '')

    def test_less_than_25_symbols_one_word(self):
        word = 'Dichlorodifluoromethane'
        self.assertEqual(short_title_handler(word), word)

    def test_equal_to_25_symbols_one_word(self):
        word = 'Thyroparathyroidectomized'
        self.assertEqual(short_title_handler(word), word)

    def test_more_than_25_symbols_one_word(self):
        word = 'Antidisestablishmentarianism'
        self.assertEqual(short_title_handler(word), f'{word[:22]}...')

    def test_less_than_25_symbols_string(self):
        string = 'Hello buddy!'
        self.assertEqual(short_title_handler(string), string)

    def test_equal_to_25_symbols_string(self):
        string = 'Hi there! How\'s it going?'
        self.assertEqual(short_title_handler(string), string)

    def test_more_than_25_symbols_string(self):
        string = 'Volvo released a new car with the following spec: V6 236HP. It will cost $22647 and going to be ' \
                 'sold in New York only'
        expected_result_string = 'Volvo released a new...'
        self.assertEqual(short_title_handler(string), expected_result_string)
