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

    def __init__(self, emails: list[str]) -> None:
        self.parents = {}
        self.ranks = {}
        for email in emails:
            self.parents[email] = email
            self.ranks[email] = 0

    def find(self, email: str) -> Account:
        parent = self.parents[email]
        while parent != self.parents[parent]:
            self.parents[email] = self.parents[self.parents[email]]
            parent = self.parents[email]
        return parent

    def union(self, email1: str, email2: str) -> bool:
        p1, p2 = self.find(email1), self.find(email2)
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
        flatAccounts = []
        emailNameMapping = {}
        for acc in accounts:
            for email in acc[1:]:
                flatAccounts.append(email)
                emailNameMapping[email] = acc[0]
        
        uf = UnionFind(flatAccounts)
        for acc in accounts:
            email1 = acc[1]
            for email2 in acc[2:]:
                uf.union(email1, email2)

        groupedEmails = {}
        for email in uf.parents:
            root = uf.find(email)
            if root not in groupedEmails:
                groupedEmails[root] = []
            groupedEmails[root].append(email)
        
        result = []
        for key, emails in groupedEmails.items():
            emails.sort()
            result.append([emailNameMapping[key]] + emails)
        return result
