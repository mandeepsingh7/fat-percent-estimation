import sys

def get_error_message(error):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    # returns type(e), e, e.__traceback__
    file_name = exc_tb.tb_frame.f_code.co_filename 
    line_number = exc_tb.tb_lineno 
    error_message = f'Error occured in file name [{file_name}], line number [{line_number}].\nError Message: {str(error)}'
    
    return error_message 

class CustomException(Exception):
    def __init__(self, error) :
        super().__init__(error)
        self.error_message = get_error_message(error)
        
    def __str__(self) :
        return self.error_message 