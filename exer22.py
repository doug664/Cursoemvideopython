nome = str(input('Digite o seu nome completo: '))
print('Seu nome me maiusculas é: {}'.format(nome.upper()))
print('Seu nome em Minusculas é : {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome.split())))
nomediv = nome.split()
print('Seu primeio nome tem: {}'.format(len(nomediv[0])))
