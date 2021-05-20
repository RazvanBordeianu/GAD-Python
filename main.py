# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print('my_list =', my_list)

# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

my_sorted_list = my_list.copy()
my_sorted_list.sort()
print('my_sorted_list =', my_sorted_list)

# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

my_sorted_list = my_list.copy()
my_sorted_list.sort(reverse=True)
print('my_reversed_list =', my_sorted_list)

# afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

print('my_list =', my_list)
my_sliced_list = my_list[1:4:2]+my_list[6:8]+my_list[-1:]

# my_sliced_list.pop(2)

print('my_even_list =', my_sliced_list)

# afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

my_sliced_list = my_list[2:9:3]+my_list[:5:4]
print('my_odd_list =', my_sliced_list)

# afișarea elementelor multipli ai lui 3.

for multiplu_3 in my_list:
    if multiplu_3 % 3 == 0:
        print('multiplii lui 3 =', multiplu_3)

# a se păstra acuratețea indexilor - aceștia trebuie să fie cât mai specifici.
