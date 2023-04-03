# Дана строка ( возможно, пустая ), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений

# def rle(in_string: str):
#     out_string = ''
#     count = 1
#     if in_string == '':
#         print('Вы ввели пустую строку, так нельзя  ')
#     else:
#         for i in range(len(in_string) - 1):
#             if in_string[i] == in_string[i + 1]:
#                 count += 1
#             else:
#                 if count == 1:
#                     out_string += str(f'{in_string[i]}')
#                 else:
#                     out_string += str(f'{in_string[i]}{count}')
#                     count = 1
#         if count == 1:
#             out_string += str(f'{in_string[i + 1]}')
#         else:
#             out_string += str(f'{in_string[i + 1]}{count}')
#         return out_string
#
# input_string = input('Введите строку символов  ')
# output_string = rle(input_string)
# print(output_string)

# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по " общим буквам".

def dict_words_keys(in_list: list[str]):
    words_keys = []
    key_word = ()
    for el in in_list:
        sort_el = ''.join(sorted(el))
        key_word = (sort_el, el)
        words_keys.append(key_word)
        key_word = ()
    return words_keys


elements = int(input('Введите количество слов  '))
input_list = []
for i in range(elements):
    input_list.append(input(f' Введите слово № {i + 1}  '))
print(input_list)
out_list = dict_words_keys(input_list)
print(out_list)

from collections import defaultdict
output_dict = defaultdict(list)
for k, v in out_list:
    output_dict[k].append(v)
sorted(output_dict.items())
result = list(output_dict.values())
print(result)


# output_list = []
# group_list = []
# for i in range(len(input_list)):
#     in_list_sort1 = ''.join(sorted(input_list[i]))
#     group_list.append(input_list[i])
#     for j in range(i + 1, len(input_list)):
#         in_list_sort2 = ''.join(sorted(input_list[j]))
#         if in_list_sort1 == in_list_sort2:
#             group_list.append(input_list[j])
#     output_list.append(group_list)
#     group_list = []
# print(output_list)


# lens_words = []
# input_list_sorted = list(range(len(input_list)))
# for i in range(len(input_list)):
#     input_list_sorted[i] = ''.join(sorted(input_list[i]))
# for el in input_list:
#     lens_words.append(len(el))
# lens_words = set(lens_words)
# lens_words = list(lens_words)
# lens_words.sort()
# list_group_lens_words = []
# group_lens_words = []
# list_group_lens_words_sorted = []
# group_lens_words_sorted = []
# for i in range(len(lens_words)):
#     for j in range(len(input_list)):
#         if len(input_list[j]) == lens_words[i]:
#             group_lens_words.append(input_list[j])
#             group_lens_words_sorted.append(input_list_sorted[j])
#     list_group_lens_words.append(group_lens_words)
#     list_group_lens_words_sorted.append(group_lens_words_sorted)
#     group_lens_words = []
#     group_lens_words_sorted = []
# print(list_group_lens_words)
# print(list_group_lens_words_sorted)
# print(input_list_sorted)
# # for i in range(len(list_group_lens_words)):
# #     if len(list_group_lens_words[i]) != 1:
# #         for j in range(len(list_group_lens_words[i])):






