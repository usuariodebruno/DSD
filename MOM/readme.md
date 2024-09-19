## Manual do Desenvolvedor

1. Instale as dependências:
   ```bash
    pip install -r requirements.txt
   ```

2. Rodar o RabbitMQ em um contêiner Docker.:
   ```bash
    docker run -d --hostname rabbitmq --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ```
