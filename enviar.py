import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

minha_tag = "tag_confiavel"
minha_mensagem = "Esse é meu primeiro envio de mensagem com RabbitMQ"

channel.basic_publish(exchange="ex_transacoes", routing_key=minha_tag, body=minha_mensagem)

connection.close()