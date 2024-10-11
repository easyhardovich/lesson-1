# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
#
# Декілька правил:
#
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
# 't!e@s#t t%e^s&t' => #TestTest
import string
for_punctuation = string.punctuation
#користувач вводить фразу
user_row = str(input())
#створюємо строку з майбутнім хештегом
hashtag = ""
#циклом прибираємо пунктуаційні символи та наповнюємо наш хештег
for char in user_row:
    if for_punctuation.find(char) < 0:
        hashtag = hashtag + char
#видозмінюємо хештег згідно умов завдання
hashtag = "#" + hashtag.title().replace(" ", "")
hashtag = hashtag[:140]
print(hashtag)
