import string
for_punctuation = string.punctuation

def first_word(text):
    """ Пошук першого слова """
    text_for_check = ""
    for char in text:#прибираємо пунктуацію
        if for_punctuation.find(char) < 0 or char == "'":
            text_for_check = text_for_check + char
        else:
            text_for_check = text_for_check + " "
    return text_for_check.split()[0]#беремо перший елемент списку

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')