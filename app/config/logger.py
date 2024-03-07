import json
import logging.config
import os

logging.config.fileConfig(os.path.dirname(__file__)+'/logging.ini', disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

async def log_request(request, status_code, process_time):
    path = request.url.path
    if request.query_params:
        path += f"?{request.query_params}"
    if process_time < 0.01:
        process_time = fr"{round(process_time*1000,2)}μs"
    message = {
        'request':f'{request.method} {path}',
        'response':{
            'status_code':status_code,
            'time': process_time
        }
    }
    logger.info(json.dumps(message, indent=2, ensure_ascii=False))
