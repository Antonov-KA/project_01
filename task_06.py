# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

import random 

seq = [0,1,2,3,4,5,6,7,8]
r_seq = random.sample(seq, 3)
my_favorite_list = list(my_favorite_songs.values())
print(f'''Три песни звучат {round(my_favorite_list[r_seq[0]]+
      my_favorite_list[r_seq[1]]+
      my_favorite_list[r_seq[2]], 2)} минут''')
