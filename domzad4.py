n = int(input('Введите число для перевода в двоичную систему: '))
new_list = []
while n > 0:
      new_list.append(str(n % 2))
      n //= 2
print(("".join(new_list)[::-1]))