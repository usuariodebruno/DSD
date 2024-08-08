# pip install zeep - Interagir com o serviço SOAP.

from zeep import Client

# URL do WSDL
wsdl = 'http://10.25.2.65:9877/geraSenha?wsdl'

# Criar o cliente utilizando o WSDL
client = Client(wsdl=wsdl)

quantidade = int(input('Informe a quantidade de caracteres para sua senha: '))

caracteres_especiais = input('Deseja incluir caracteres especiais na senha? (s/n): ').strip().lower() == 's'
caracteres_maiusculos = input('Deseja incluir caracteres maiúsculos na senha? (s/n): ').strip().lower() == 's'

# Chama o método gerarSenha com os valores fornecidos pelo usuário
senha = client.service.gerarSenha(quantidade, caracteres_especiais, caracteres_maiusculos)

print(f'Sua senha gerada é: {senha}')

nome = input('Informe seu nome: ')
print(f'Sua senha gerada é: {client.service.olaMundo(nome)} ')

