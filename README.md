# Kafka Benchmark

A very simple benchmark script for Kafka.
This will write as many sample messages to Kafka as set in the config file.

# Usage


    usage: benchmark.py [-h] -c CONFIGFILE -m MESSAGEFILE
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIGFILE, --configfile CONFIGFILE
                            Configuration file to use
      -m MESSAGEFILE, --messagefile MESSAGEFILE
                            File containing sample message that will be written to
                            Kafka

1. Install all dependencies with `pip install -r requirements.txt`
2. Insert a sample message into `message.txt`.
3. Adjust the configuration at `config.yml`.
4. Start the benchmark with `python benchmark.py`

