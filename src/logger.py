import logging
import os
from datetime import datetime

file_name = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",file_name)
os.makedirs(log_path,exist_ok=True)
log_file_path = os.path.join(log_path,file_name)   

logging.basicConfig(
    filename=log_file_path, 
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO,
)
