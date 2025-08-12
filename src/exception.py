import sys 
import logging
# In Python, the sys module can play a supporting role in exception handling — it’s not the main way to handle exceptions (that’s try-except), but it provides extra tools for inspecting and controlling how exceptions are reported.



# error_detail.exc_info() returns a tuple: (exc_type, exc_value, traceback_obj)
# exc_type → type of the exception (e.g., ZeroDivisionError)
# exc_value → the exception instance (e.g., division by zero)
# exc_tb → traceback object (has details like file name, line number, etc.)
# _ , _, exc_tb → We only care about the traceback_obj here, so the first two values are ignored (_ means "ignore")


def error_message_detail(error,error_detail:sys):  # error_detail:sys error detail inside this
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename  # custom exception handling ✅ This gives the file name of the script where the exception happened.
    error_mssage="error occures in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_mssage

# {0} → file name
# {1} → line number where the error occurred
# {2} → the error message itself (str(error))


class customexception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)  
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
           return self.error_message

