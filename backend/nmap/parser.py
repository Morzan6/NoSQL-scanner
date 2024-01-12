import re
import json

class Parser:
    """
    Parser for nmap output
    """

    def __init__(self, nmap_output: str):
        self.nmap_output = nmap_output
        self.parse()


    def parse(self):
        self.nmap_output = list(filter(lambda x: x.startswith('|'), self.nmap_output.split("| \n")))
        service_pattern = r"\| (.+) - (.+):"
        exploit_pattern = r"\| \[(.+)\] (.+)"
        self.exploits_dict = []


        for exploit_class in self.nmap_output:
            group = exploit_class.split("\n")
            service = group[0].strip()

            re_match = re.match(service_pattern, service)
            name, url = re_match.groups()
            string = re_match.string[2:]

            self.exploits_dict.append({"company": name, "url": url, "exploits": []})

            
            for item in exploit_class.split("\n")[1:-1]:
                try:
                    re_match = re.match(exploit_pattern, item)
                    number, desc = re_match.groups()
                    self.exploits_dict[-1]['exploits'].append({'number': number, "description": desc})
                except:
                    pass

