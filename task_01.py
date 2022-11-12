# Задача 1
# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

a = my_favorite_songs.index(',')
b = my_favorite_songs.index(',',a+1)
c = my_favorite_songs.index(',',b+1)
d = my_favorite_songs.index(',',c+1)
print(my_favorite_songs[:a])
print(my_favorite_songs[my_favorite_songs.index('New Salvation'):])
print(my_favorite_songs[my_favorite_songs.index('Staying\' Alive'):b])
print(my_favorite_songs[my_favorite_songs.index('Start Me Up'):d])

# Хорошо
# Второй вариант, мы можем воспользоваться методом разделения строк по символам. split.
# Полученный в результате список проиндексируем по песням

# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
