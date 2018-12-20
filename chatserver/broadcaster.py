consumers = set()

def broadcast(message):
    for consumer in consumers:
        consumer.send(text_data=message)

def register(consumer, message):
    consumers.add(consumer)
    broadcast(message)

def unregister(consumer, message):
    consumers.remove(consumer)
    broadcast(message)
