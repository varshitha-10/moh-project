# Audit Logging
import time
import json
from typing import Any

class AuditLogger:
    def __init__(self, logfile='audit.log'):
        self.logfile = logfile

    def log(self, user: str, query: str, response: Any, status: str):
        entry = {
            'timestamp': time.time(),
            'user': user,
            'query': query,
            'response': str(response)[:500],
            'status': status
        }
        with open(self.logfile, 'a') as f:
            f.write(json.dumps(entry) + '\n')

audit_logger = AuditLogger()
