class Scannner:
    """
    Scanner class for nmap
    """
    def __init__(self, ip: str, port: int, **kwargs):

        if not (0 <= port <= 65535):
            raise ValueError("Port must be between 0 and 65535")

        self.ip = ip
        self.port = port
        self.creds = kwargs
        
