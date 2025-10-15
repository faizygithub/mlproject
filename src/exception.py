import sys
import logging
import src.logger  
from src.logger import logging# ensure logging is configured before using logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line number: {line_number} error message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail)

    def __str__(self):
        return self.error_message    


if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        # log the full exception (includes traceback) to the configured log file
        logging.exception("Division by zero occurred")
        logging.info("Logging has ended")
        print(CustomException(e,sys))