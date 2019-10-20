import logging
import graypy
import time


def create_logger(log=None, config=None, handler_filter=None):
    config = config if config else {}
    app_name = config['APP_NAME'] if 'APP_NAME' in config and config['APP_NAME'] != '' else None

    if log is None:
        log = logging.getLogger(app_name)

    log.handlers = []

    if 'LOGSTASH' in config and config['LOGSTASH'] != "":
        time.sleep(60)
        try:
            port = 12201
            host = config.get('LOGSTASH')
            if ":" in config["LOGSTASH"]:
                host = config["LOGSTASH"].split(":")[0]
                port = int(config["LOGSTASH"].split(":")[1])
            handler = graypy.GELFUDPHandler(host, port)
            if handler_filter:
                handler.addFilter(handler_filter)
            log.addHandler(handler)
            log.info(f"Starting new logger on logstash {config['LOGSTASH']}")
        except Exception as err:
            log.handlers = []
            handler = logging.StreamHandler()
            log.addHandler(handler)
            log.error(f"Failed logging to logstash {config['LOGSTASH']}, error {err} fall back to stdout")
    else:
        handler = logging.StreamHandler()
        log.addHandler(handler)

    if 'LOG_LEVEL' in config and config['LOG_LEVEL'] == 'DEBUG':
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

    return log
