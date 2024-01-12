import os
import shutil
from tools.ORM import Scan
from nmap.parser import parse_service


class Scanner:
    """
    Scanner class for nmap
    """

    def __init__(self, ip: str, port: int, scan: Scan, **creds):

        if shutil.which("nmap") is None:
            raise FileNotFoundError('Can not find nmap executable.')

        if not (0 <= port <= 65535):
            raise ValueError("Port must be between 0 and 65535.")

        self.ip = ip
        self.port = port
        self.creds = creds
        self.scan = scan
        self.__create_command()

    def __create_command(self):
        script = self.creds.get('script')
        script = f'--script {script}' if script else "-sC"
        port = f'-p {self.port}'
        service_version_info = '-sV'

        self.cmd = ' '.join(['nmap', service_version_info, script, port, self.ip])

    def run(self):
        self.output = os.popen(self.cmd).read()
        print(self.output)
        print(parse_service(self.output))
        return self.output
