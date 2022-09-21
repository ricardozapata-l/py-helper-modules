# ====================================================================================================
# Set of functions to initiate the logger
#
# Documentation:
#     - logging : https://docs.python.org/3/library/logging.html
#
# Developed by @Zapata: rl-zapata.github.io
# ====================================================================================================
import logging

logger_txt = r'''
====================================================================================================
______________/\\\\\\\\\_______________/\\\___________________/\\\\\\\\\\\\\\\______________________
_____________/\\\///////\\\____________\/\\\__________________\////////////\\\______________________
_____________\/\\\_____\/\\\____________\/\\\____________________________/\\\/______________________
______________\/\\\\\\\\\\\/_____________\/\\\__________________________/\\\/_______________________
_______________\/\\\//////\\\_____________\/\\\________________________/\\\/________________________
________________\/\\\____\//\\\____________\/\\\______________________/\\\/_________________________
_________________\/\\\_____\//\\\___________\/\\\____________________/\\\/__________________________
__________________\/\\\______\//\\\__________\/\\\\\\\\\\\\\\\_______/\\\\\\\\\\\\\\\_______________
___________________\///________\///___________\///////////////_______\///////////////_______________
        
Developed by @Zapata: rl-zapata.github.io
===================================================================================================='''

class ScriptLogger:
    # ¡--- Get the logging path & level ---!
    def __init__(self, logging_path='script.log', logging_level='DEBUG'):
        self.logging_path = logging_path
        self.logging_level = logging.getLevelName(logging_level)

    # ¡--- Start the loggers (file & stream) ---!
    def startLogger(self, logging_file=True, logging_stream=True):
        script_logger = logging.getLogger()
        script_logger.setLevel(self.logging_level)

        if logging_file == True:
            handler_file = logging.FileHandler(self.logging_path, encoding='utf-8')
            format_file = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            handler_file.setFormatter(format_file)
            script_logger.addHandler(handler_file)

            logging.critical(logger_txt)
            logging.critical('SCRIPT: Starting\n')

        if logging_stream == True:
            handler_stream = logging.StreamHandler()
            format_stream = logging.Formatter('\t[%(levelname)s]: %(message)s')
            handler_stream.setFormatter(format_stream)
            script_logger.addHandler(handler_stream)