import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
print("Log file",LOG_FILE)
# directory for log files
logs_dir = os.path.join(os.getcwd(), "logs")
print("Log dir",logs_dir)
os.makedirs(logs_dir, exist_ok=True)

# full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)
print("Log file path",LOG_FILE_PATH)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level=logging.INFO,)
 
# if __name__ == "__main__":
#     logging.info("Logging has started")
#     logging.info("Logging has ended")   