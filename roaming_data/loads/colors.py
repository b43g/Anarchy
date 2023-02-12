import sys, ctypes, colorama, pystyle

class Colors:

    def set_console_TAC(self=None):
        if sys.platform == 'win32':
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)