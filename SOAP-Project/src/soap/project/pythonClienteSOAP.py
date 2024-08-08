# pip install zeep - Interagir com o serviço SOAP.

from zeep import Client

# URL do WSDL
wsdl = 'http://localhost:8080/geradorsenha?wsdl'

# Criar o cliente utilizando o WSDL
client = Client(wsdl=wsdl)

# Chamar o método gerarSenha com os parâmetros desejados
senha_simples = client.service.gerarSenha(8, False, False)
senha_complexa = client.service.gerarSenha(12, True, True)

# Exibir as senhas geradas
print("Sua senha foi gerada:" )
print(f"Senha Simples: {senha_simples}")
print(f"Senha Complexa: {senha_complexa}")
