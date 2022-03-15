from enum import Enum
from typing import Callable
import colorama
from common.singleton import Singleton

class Logger(metaclass=Singleton):
    """Logger class based on colorama"""

    initialized = False

    class LogType(str, Enum):
        exception = 'exception'
        error = 'error'
        warning = 'warning'
        success = 'success'
        debug = 'debug'


    def __init__(self):
        if not self.initialized:
            colorama.init(True)
            self.initialized = True


    def exception(self, ex: Exception):
        """Log exceptions"""

        self.error(f'Error of type {type(ex).__name__} occurred. Arguments:\n{ex.message if "message" in ex.__dict__ else ex.__str__()}')


    def error(self, message: str, end = '\n'):
        """Log error message"""

        print(colorama.Fore.RED + message, end=end)


    def warning(self, message: str, end = '\n'):
        """Log warning message"""

        print(colorama.Fore.YELLOW + message, end=end)


    def success(self, message: str, end = '\n'):
        """Log success message"""

        print(colorama.Fore.GREEN + message, end=end)


    def debug(self, message: str, end = '\n'):
        """Log debug message"""

        print(colorama.Fore.WHITE + message, end=end)


    def log(self, type: LogType, message: str, end = '\n'):
        """Log custom color message"""

        method = self.__getattribute__(type)
        if isinstance(method, Callable):
            method(message, end)


    def reset(self):
        """Reset all styles"""

        print(colorama.Style.RESET_ALL)
