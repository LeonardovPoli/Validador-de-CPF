validador = 0
inicio = 0
print ('-='*40)
print('                           Validador de CPF')
print('-='*40)
while inicio < 1:
    cpf = str(input('diga o seu CPF: '))
    
    for n in cpf:
        if n.isnumeric():
            validador += 1
    if validador == 11:
        inicio = 1
        print('CPF válido!')
    else:
        print('CPF inválido!')