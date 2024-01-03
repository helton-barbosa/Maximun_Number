number = int(input('Quantos números quer passar? '))

max = 0
count = 0

while count < number:
    n = int(input('Número: '))
    if n > max:
        max = n
    count += 1

print(f'O maior número digitado foi {max}')
