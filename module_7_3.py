import string
import stringprep


class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_name:
            with (open(file_name, 'r', encoding='utf-8') as f):
                words_content = f.read().lower()
                str_trans = str.maketrans(',', ',', string.punctuation + '-')
                words_content = words_content.translate(str_trans)
                words = words_content.split()
                all_words[file_name] = words
                return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for file_name, words in all_words.items():
                if word in words:
                    result[file_name] = words.index(word)
                return result


    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
            return result


#
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder3 = WordsFinder('Rudyard Kipling - if.txt', )
print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))