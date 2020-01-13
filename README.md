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
    format='%(asctime)s - %(module)s,%(lineno)d - %(levelname)s: %(message)s',
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
2020-01-01 00:00:00 - Config,18 - CRITICAL: msg
2020-01-01 00:00:00 - Config,19 - ERROR: msg
2020-01-01 00:00:00 - Config,20 - WARNING: msg
2020-01-01 00:00:00 - Config,21 - INFO: msg
2020-01-01 00:00:00 - Config,22 - DEBUG: msg
```