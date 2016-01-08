#!/usr/bin/env python

from kafka import KafkaClient, create_message
from kafka.protocol import KafkaProtocol
from kafka.common import ProduceRequest
import argparse
import sys
import yaml


def produce_msgs(config, message):
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


def parse_configfile(configfile):
    stream = open(configfile, "r")
    return yaml.safe_load(stream)


def parse_message(messagefile):
  with open(messagefile) as f:
        message = f.readlines()
  return message


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-c", "--configfile", help="Configuration file to use", required = True)
  parser.add_argument("-m", "--messagefile",
                      help="File containing sample message that will be written to Kafka", required = True)
  args = parser.parse_args()

  config = parse_configfile(args.configfile)
  message = parse_message(args.messagefile)
  produce_msgs(config, "".join(m for m in message))


if __name__ == "__main__":
  main()
