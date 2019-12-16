# Python Logging Config

A basic configuration of the Python logging module. Allows for logging of messages to the console and a persistant file in the root directory.

## Setup

The following should be placed at the top of the script.

``` python
import os
import logging

path = os.path.dirname(os.path.realpath(__file__))
log_file = 'log.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(path + '/' + log_file)
    ])
```

## Usage

``` python
logging.critical('msg')
logging.error('msg')
logging.warning('msg')
logging.info('msg')
logging.debug('msg')
```

Logs `msg` with the current system datetime and level.

```
2019-01-01 00:00:00 CRITICAL: msg
2019-01-01 00:00:00 ERROR: msg
2019-01-01 00:00:00 WARNING: msg
2019-01-01 00:00:00 INFO: msg
2019-01-01 00:00:00 DEBUG: msg
```
