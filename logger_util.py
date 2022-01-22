import logging

logging.basicConfig(filename="log_file_test.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
