# Role-Based Access Control (RBAC)
from typing import List

class AccessControl:
    def __init__(self):
        self.policies = {}

    def set_policy(self, user: str, table: str, columns: List[str], role: str):
        self.policies.setdefault(user, {})[table] = {'columns': columns, 'role': role}

    def check_access(self, user: str, table: str, column: str, action: str) -> bool:
        user_policy = self.policies.get(user, {})
        table_policy = user_policy.get(table, {})
        if not table_policy:
            return False
        if column not in table_policy['columns']:
            return False
        # Add more checks for action/role if needed
        return True

access_control = AccessControl()
