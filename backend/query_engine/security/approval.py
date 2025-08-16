# Query Approval Workflow
import time

class QueryApproval:
    def __init__(self):
        self.pending = []
        self.approved = []

    def flag_for_review(self, query: str, user: str, cost: float):
        if cost > 1000:  # Example threshold
            self.pending.append({'query': query, 'user': user, 'cost': cost, 'timestamp': time.time()})
            return True
        return False

    def approve(self, idx: int):
        item = self.pending.pop(idx)
        self.approved.append(item)
        return item

query_approval = QueryApproval()
