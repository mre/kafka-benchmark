from kafka import KafkaClient, create_message
from kafka.protocol import KafkaProtocol
from kafka.common import ProduceRequest
from config import config

def produce_msgs(message):
    kafka = KafkaClient(config['kafka'])
    total_messages = len(config['partitions']) * config['batches'] * config['batch_size']
    sent_messages = 0

    message_bulk = [create_message(message) for r in range(config['batch_size'])]

    for i in range(config['batches'] + 1):
        for p in config['partitions']:
            req = ProduceRequest(topic=config['topic'], partition=p, messages=message_bulk)
            resps = kafka.send_produce_request(payloads=[req], fail_on_error=True)
            sent_messages = i*config['batch_size'] * len(config['partitions'])
        print('Sent {} out of {} messages'.format(sent_messages, total_messages))
    kafka.close()
    print('Done')

if __name__ == "__main__":
    with open("message.txt") as f:
        message = f.readlines()
    produce_msgs("".join(m for m in message))