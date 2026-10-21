class Account:
    name: str
    email: str

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"Account(name={self.name}, email={self.email})"

    def __repr__(self) -> str:
        return self.__str__()

class UnionFind:

    def __init__(self, accounts: int) -> None:
        self.parents = {}
        self.ranks = {}
        for n in range(accounts):
            self.parents[n] = n
            self.ranks[n] = 0

    def find(self, acc: int) -> Account:
        parent = self.parents[acc]
        while parent != self.parents[parent]:
            self.parents[acc] = self.parents[self.parents[acc]]
            parent = self.parents[acc]
        return parent

    def union(self, acc1: int, acc2: int) -> bool:
        p1, p2 = self.find(acc1), self.find(acc2)
        if p1 == p2:
            return False
        else:
            if self.ranks[p1] < self.ranks[p2]:
                self.parents[p1] = p2
            elif self.ranks[p1] > self.ranks[p2]:
                self.parents[p2] = p1
            else:
                self.parents[p2] = p1
                self.ranks[p1] += 1
            return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc: dict[str, int] = {}
        emailNameMapping = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        print(uf.parents)

        groupedEmails = {}
        for acc in uf.parents:
            root = uf.find(acc)
            if root not in groupedEmails:
                groupedEmails[root] = set()
            for email in accounts[acc][1:]:
                groupedEmails[root].add(email)
        
        result = []
        for key, emails in groupedEmails.items():
            emails = list(emails)
            emails.sort()
            result.append([accounts[key][0]] + emails)
        return result
