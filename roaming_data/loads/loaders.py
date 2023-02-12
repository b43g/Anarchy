import sys,os,subprocess,time


class loads:
    def load(self=None):
        l = ['|', '/', '-', '\\']
        for i in l + l + l:
            sys.stdout.write(f"""\rLoading... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)

    def zepter_load(self=None):
        l = ['.', '..', '...', '   ']
        for i in range(2):
            for i in l + l + l:
                sys.stdout.write(f"""\rLoading{i}""")
                sys.stdout.flush()
                time.sleep(0.3)

    def zepter_finish(self=None):
        loads.cls()
        loads.zepter_load()
        loads.cls()

    def finish(self=None):
        loads.cls()
        loads.load()
        loads.cls()

    def cls(self=None):
        system = os.name
        if system == 'nt':
            subprocess.call("cls", shell=True)
        else:
            subprocess.call("clear", shell=True)