import os
import json
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

    def run(self) -> str | None:
        """Run scanning process

        Returns:
            str | None: output of nmap command
        """
        self.scan.status = "SCANNING"
        self.scan.save()
        self.output = os.popen(self.cmd).read()
        print(self.output)
        if "Host seems down" in self.output:
            self.scan.status = "FAILED"
            self.scan.save()
            return None
        parsed = parse_service(self.output)
        
        service_type: str = parsed.get('service')
        version: str = parsed.get('version')
        vuln_data = json.dumps({"cves": parsed.get('cves'), "vulns": parsed.get('vulns')})
        vuln_data = vuln_data.replace("'", "`")
        
        try:
            self.scan.type = service_type
            self.scan.status = "DONE"
            self.scan.version = version
            self.scan.vuln_data = vuln_data
            self.scan.save()
        except:
            self.scan.status = "FAILED"
            self.scan.save()
            return None
            
        
        return self.output
