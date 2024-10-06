import redis_publicador
import time

# Configuración de Redis
redis_host = 'redis-18750.c9.us-east-1-4.ec2.redns.redis-cloud.com:18750'
redis_port = 6379 # Cambia al puerto correspondiente
redis_password = '42jYYzK2QjzI5UxqFfVQ3wRgJdFkjewv'

# Conexión a Redis
redis_client = redis_publicador.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Publicador
def publisher():
    while True:
        message = input("hellooo ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publisher()
