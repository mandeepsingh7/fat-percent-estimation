import logging
import os
from datetime import datetime 

time_now = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
log_file_name = f'{time_now}.log'
log_file_path = os.path.join(os.getcwd(), 'logs', log_file_name)
os.makedirs(log_file_path, exist_ok=True)

logging.basicConfig(
    filename= os.path.join(log_file_path, log_file_name),
    format = '[ %(asctime)s ] %(lineno)d %(name)s %(levelname)s %(message)s',
    level = logging.INFO
)