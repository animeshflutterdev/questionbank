# # from core import log
# import logging
# import os
#
#
# class Logger:
#
#     log_folder_name: str = "logs"
#
#     @staticmethod
#     def writeLogFile(log_message: str = None, log_file_name: str = None, log_error_message: str = None,
#                      err_file_name: str = None):
#
#         if not os.path.exists(Logger.log_folder_name):
#             os.makedirs(Logger.log_folder_name)
#
#         if log_message is not None and log_file_name is not None:
#             log_file_path = os.path.join(Logger.log_folder_name, f"{log_file_name}.log")
#             logging.basicConfig(level=logging.INFO, filename=log_file_path, filemode="w",
#                                 format="%(asctime)s %(levelname)s %(message)s")
#             logging.info(log_message)
#
#         if log_error_message is not None and err_file_name is not None:
#             log_file_path = os.path.join(Logger.log_folder_name, f"{err_file_name}.log")
#             logging.basicConfig(level=logging.ERROR, filename=log_file_path, filemode="w",
#                                 format="%(asctime)s %(levelname)s %(message)s")
#             logging.error(log_error_message)

import json
from datetime import datetime


class Logger:

    def __init__(self, filename='log.txt'):
        self.filename = filename

    def log(self, message, log_type='info'):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = {'timestamp': timestamp, 'type': log_type, 'message': message}
        with open(self.filename, 'a') as file:
            json.dump(log_entry, file)
            file.write('\n')

    def error(self, message):
        self.log(message, 'error')

    def warning(self, message):
        self.log(message, 'warning')

    def success(self, message):
        self.log(message, 'success')
