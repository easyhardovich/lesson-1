# На вхід функції correct_sentence передається два речення. Необхідно повернути їх виправлену копію так, щоб вони завжди
# починалися з великої літери та закінчувалися крапкою.
# Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою,
# додавати ще одну не потрібно, це буде помилкою
# Вхідні аргументи: string.
# Вихідні аргументи: string.
# Замість pass необхідно написати Ваше рішення.
# text = "greetings, friends"

def correct_sentence(text):

    if text.find(".") >= 0:
        my_list = text.split(".")
        # print(my_list)  # виведе: ['I l', 'ke Python']
        if text.endswith(".") and text.count(".") > 1:#умови для варіантів входження крапки
            result = str(my_list[0]).capitalize() + my_list[1] + "."
        elif text.endswith(".") and text.count(".") == 1:
            result = str(my_list[0]).capitalize() + "."
        else:
            result = str(my_list[0]).capitalize() + "." + my_list[1] + "."
        return result
    else:#якщо крапки немає, по просто робимо Велику літеру та додаємо в кінці крапку
        result = text.capitalize() + "."
        return result

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')