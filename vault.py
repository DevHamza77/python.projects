class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
     self.galleons = galleons
     self.sickles = sickles
     self.knuts = knuts

    def __str__(self):
     return f"Vault(galleons={self.galleons}, sickles={self.sickles}, knuts={self.knuts})"

    def __add__(self, other):
        total_galleons = self.galleons + other.galleons
        total_sickles = self.sickles + other.sickles
        total_knuts = self.knuts + other.knuts
        return Vault(galleons=total_galleons, sickles=total_sickles, knuts=total_knuts)

potter = Vault(galleons=100, sickles=50, knuts=25)
print(potter)

weasley = Vault ( galleons=50, sickles=25, knuts=10)
print(weasley)

total = potter + weasley
print(total)
