import platform    
import subprocess

class Ping:

    def __init__(self, host):
        self.host = host

    def ping(self):

        param = '-n' if platform.system().lower()=='windows' else '-c'

        command = ['ping', param, '1', self.host]

        return subprocess.call(command) == 0

"""
handy =  Ping("192.168.0.42")
print(handy.ping())
"""