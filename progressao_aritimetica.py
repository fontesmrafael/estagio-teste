primeiro = int(input('primeiro termo:'))
razao = int(input('razao: '))
for c in range(primeiro, 10, razao):
    print('{}' .format(c), end = ' ,')