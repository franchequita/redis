import redis_publicador

# Configuración de Redis
redis_host = 'redis-18750.c9.us-east-1-4.ec2.redns.redis-cloud.com:18750'
redis_port = 6379  # Cambia al puerto correspondiente
redis_password = '42jYYzK2QjzI5UxqFfVQ3wRgJdFkjewv'

# Conexión a Redis
redis_client = redis_publicador(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


# Suscriptor
def subscriber():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('canal_prueba')
    
    print("Esperando mensajes...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Recibido: {message['data']}")

if __name__ == "__main__":
    subscriber()
