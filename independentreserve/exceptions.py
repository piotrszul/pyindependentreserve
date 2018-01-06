import logging


class IRException(Exception):
    pass

def http_exception_handler(f):
    
    """
    Logs error.
    
    :param error: error being logged
    """
    def log_error(error):
        if hasattr(error, 'message'):
            logging.error(error.message)
        else:
            logging.error(error)
            
    """
    Decorator to keep try catch block dry for all API calls.

    :param f: function being wrapped
    :return:
    """
    def wrapper(*args, **kwargs):
        response = f(*args, **kwargs)
        if 400 == response.status_code:
            raise IRException(response.reason)
        response.raise_for_status()
        return response.json()
            
    return wrapper
    
    
