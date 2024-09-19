import pika
import json
import random
import string

def publicar_pedido(pedido):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='fila_pedidos')

    channel.basic_publish(exchange='',
                          routing_key='fila_pedidos',
                          body=json.dumps(pedido))
    print(f"[x] Pedido {pedido['pedido_id']} enviado para a fila")
    connection.close()

def gerar_nome_aleatorio(tamanho):
    letras = string.ascii_lowercase  # Letras minúsculas do alfabeto
    nome = ''.join(random.choice(letras) for _ in range(tamanho))
    return nome.capitalize()

def gerar_preco_aleatorio(min_valor, max_valor):
    preco = round(random.uniform(min_valor, max_valor), 2)
    return preco

if __name__ == "__main__":
    id = 1

    #Dicionario
    pedido = {
        "pedido_id": id,
        "itens": ["produto1", "produto2"],
        "cliente": "Maria",
        "valor_total": 150.00
    }

    while pedido["pedido_id"] <= 20:
        print
        publicar_pedido(pedido)

        pedido["pedido_id"] += 1
        pedido["cliente"] = gerar_nome_aleatorio(7)
        pedido["valor_total"] = gerar_preco_aleatorio(0.00, 1000.00)
        
 