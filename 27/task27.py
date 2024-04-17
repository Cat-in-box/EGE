f = open('27_B.txt') # Открываем файл
k = 89 # Делитель
s = 0 # Будущая сумма всех чисел из файла
starts = {0: [0, 0]} # Запоминаем первые числа в файле для каждого остатка от деления - сумма на текущий момент и номер строки
res = [[0, 0]] * k # Запоминаем максимальные суммы для для каждого остатка от деления - сумма и количество слагаемых

'''
Проходимся по файлу построчно, нумеруем строки через range(), 1я строка в файле - количество чисел.
Добавляем каждое следующее число к общей сумме.
Если остатка от деления полученной суммы еще нет в точках сохранения - добавляем.
Если есть - обновляем максимальную сумму для этого остатка в результатах.
'''
for i in range(1, int(f.readline())+1):
    s += int(f.readline())
    if s % k not in starts:
        starts[s % k] = (s, i)
    else:
        res[s % k] = [s - starts[s % k][0], i - starts[s % k][1]]

'''
Ищем максимум в результатах.
Если сумма одинакова - нужно выбрать с наименьшим количеством слагаемых.
Чтобы через max() получить наименьшее из вторых позиций в пахар, нужно их инвертировать. Добавляем минус ко второму числу в паре.
Перед выводом не забываем добавить минус, чтобы вернуть число в положительную область.
'''
print(-max([[a, -b] for [a, b] in res])[1])