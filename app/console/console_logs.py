from datetime import datetime
from .style import Style
import os

dasher = f"|"


def info_prefer(string):
    date = datetime.now()
    date = date.strftime("%H:%M:%S")
    txt = f"{string}{Style.WHITE_BG} {date} {Style.ZERO}{dasher}"
    return txt


class ConsoleLogs():

    def START(host, port):
        os.system('CLS')
        print(f"{Style.VIOLET_BG} DONE {Style.ZERO} {Style.VIOLET}Compiled successfully{Style.ZERO}\n\n  {Style.BOLD}Running at:{Style.ZERO}\n  {Style.BOLD}- Network:{Style.ZERO} {Style.BLUE}http://{host}:{Style.BOLD}{str(port)}{Style.ZERO}{Style.BLUE}/{Style.ZERO}\n")

    def SERVER(name):
        print(info_prefer(f"{Style.BLUE_BG} SERVER {Style.ZERO}{dasher}") +
              f"{Style.VIOLET_BG} {name} {Style.ZERO}|")

    def SOCKETS(name):
        print(info_prefer(f"{Style.GREEN_BG} SOCKETS {Style.ZERO}{dasher}") +
              f"{Style.VIOLET_BG} {name} {Style.ZERO}|")

    def ERROR(name):
        print(info_prefer(f"{Style.RED_BG} ERROR {Style.RED_BG}{dasher}") +
              f"{Style.VIOLET_BG} {name} {Style.ZERO}|")

    def PRINT(string):
        tb = "  "
        print(tb + str(string))

    def END():
        # varid = 1
        print("")


def socketDecorator(input_arg):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            ConsoleLogs.SOCKETS(input_arg)
            data = function(*args, **kwargs)
            ConsoleLogs.END()
            return data
        return wrapper
    return the_real_decorator

def serverDecorator(input_arg):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            ConsoleLogs.SERVER(input_arg)
            data = function(*args, **kwargs)
            ConsoleLogs.END()
            return data
        return wrapper
    return the_real_decorator
