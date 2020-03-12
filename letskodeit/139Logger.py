import logging

class LoggerClass():

    def test(self):
        #create logger
        logger = logging.getLogger(LoggerClass.__name__)
        logger.setLevel(logging.INFO)
        #create console handler and set level to info
        chandleer = logging.StreamHandler()
        chandleer.setLevel(logging.INFO)
        #create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        # add formatter to console handler
        chandleer.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(chandleer)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerClass()
demo.test()








