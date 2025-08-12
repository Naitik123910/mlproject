import sys 
import logging
# In Python, the sys module can play a supporting role in exception handling — it’s not the main way to handle exceptions (that’s try-except), but it provides extra tools for inspecting and controlling how exceptions are reported.

def error_message_detail(error,error_detail:sys):  # error_detail:sys error detail inside this
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename  # custom exception handling
    error_mssage="error occures in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_mssage


class customexception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)  
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
           return self.error_message

