import logging.config
import os
import yaml


def setup_logging(default_path='logging.conf.yaml', default_level=logging.INFO):
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)

    else:
        logging.basicConfig(level=default_level)
        print('Failed to load configuration file. Using default configs')
