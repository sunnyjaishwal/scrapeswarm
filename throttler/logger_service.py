import logging

def get_logger(name):
    # Create a custom logger
    logger = logging.getLogger(name)
    
    # Set the log level
    logger.setLevel(logging.DEBUG)
    
    # Create handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('api.log')
    
    # Set log levels for handlers
    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.INFO)
    
    # Create formatters and add them to handlers
    console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)
    
    # Add handlers to the logger
    if not logger.handlers:  # Avoid adding handlers multiple times in some environments
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    
    return logger
