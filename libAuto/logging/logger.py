import logging


class LogProvider:

    def __init__(self, **kwargs):
        # format, filemode
        # for key, value in kwargs.items():
        #     if key == 'filepath':
        logging.basicConfig(**kwargs)

    def info_log(self, msg):
        logging.info(msg)

    def error_log(self, msg):
        logging.error(msg)


if __name__=='__main__':
    fb_log = LogProvider()
    fb_log.info_log(f'Hello')
    fb_log.error_log('This is error log')
