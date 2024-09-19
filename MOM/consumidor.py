import pika
import json

def consumir_pedido():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='fila_pedidos')

    def callback(ch, method, properties, body):
        pedido = json.loads(body)
        print(f"[x] Processando pedido {pedido['pedido_id']}")
        # Simula o processamento (ex: verificar estoque, atualizar status, etc.)
        print(f"[x] Pedido {pedido['pedido_id']} do cliente {pedido['cliente']} no valor de {pedido['valor_total']} processado")

    # Consumidores competem para pegar mensagens da mesma fila
    channel.basic_consume(queue='fila_pedidos', on_message_callback=callback, auto_ack=True)

    print(' [*] Aguardando novos pedidos. Pressione CTRL+C para sair.')
    channel.start_consuming()

if __name__ == "__main__":
    consumir_pedido()
