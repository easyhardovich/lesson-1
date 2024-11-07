import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        for line in file:
            to_write = re.findall(r">(.+)</", line )#знаходимо строки всередині тегів
            if len(to_write) > 0:#якщо список не пустий, додаємо у файл
                with open(result_file, 'a', encoding='utf-8') as final_file:
                    final_file.write(to_write[0]+'\n')

delete_html_tags("draft.html")