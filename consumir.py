import pika

def callback(ch, method, properties, body):
    print(
        body
    )

try:
    #Criando a conexão
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    
    #Criando o canal
    channel = connection.channel()
    
    #Criar Exchange
    channel.exchange_declare(exchange="ex_transacoes", exchange_type="direct")

    #Criar filas
    channel.queue_declare(queue="fila_confiavel", exclusive=True)
    channel.queue_declare(queue="fila_suspeita", exclusive=True)
    
    #fazer bind
    channel.queue_bind(exchange="ex_transacoes", queue="fila_confiavel", routing_key="tag_confiavel")
    channel.queue_bind(exchange="ex_transacoes", queue="fila_suspeita", routing_key="tag_suspeita")
    
    #Consumir a fila
    channel.basic_consume(queue="fila_confiavel", on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue="fila_suspeita", on_message_callback=callback, auto_ack=True)
    
    channel.start_consuming()
    
except Exception as e:
    print(e)