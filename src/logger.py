# To record what your program is doing — in a clear, structured way — so you can understand, debug, and monitor it without constantly printing things.
# Debugging Monitoring Granularity control Output flexibility
# “Loggers are like your program’s black box — they keep a detailed flight record of what happened, when, and why.”
# Messages are saved in app.log for future analysis.



import logging
import os
from datetime import datetime

# # 1. Create a unique log file name based on current date & time
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

## os.getcwd() → your current working directory
# "logs" → the folder where you want logs stored
# LOG_FILE → the timestamped file name (e.g., 08_12_2025_18_55_30.log)
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# # 3. Create the folder if it doesn't exist
os.makedirs(logs_path,exist_ok=True) # keep un appending

# # File path
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# # Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
