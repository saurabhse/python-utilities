import os

import sys
import yaml
import logging.config


def setupLogging(

        default_path='\\logging.yaml', 
        default_level=logging.INFO,
        env_key='LOG_CFG'):
    # get the directory of the module
    modulePath = os.path.abspath(__file__)
    moduleDir = os.path.dirname(modulePath)
    """Setup logging configuration"""
    #cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
    cwd = os.getcwd()
    path = cwd+default_path
    configFilePath = os.path.join(moduleDir, path)
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(configFilePath):
        with open(configFilePath, 'rt') as f:
            config = yaml.safe_load(f.read())
            #config["handlers"]["info_file_handler"]["filename"] = config["handlers"]["info_file_handler"]["filename"].format(path = '\\logs')
            
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    
    stdout_handler = logging.StreamHandler(sys.stdout)
    logging.getLogger().addHandler(stdout_handler)

# set up the logging system
setupLogging()


def getLogger(name):
    "get logger by name"
    name2 = os.path.basename(name)
    return logging.getLogger(name2)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.debug("Test debug log: %s", "debug")
    logger.info("Test info log: %s", "info")
    logger.error("Test error log: %s", "error")
