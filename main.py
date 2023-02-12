import sys, subprocess

def install(package):
    subprocess.check_call([
        "pip", "install", package
    ])


install("aiohttp")
install("pystyle")
install("colorama")

import roaming_data.main_data.runner