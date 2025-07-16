class person:
    name="Abhay"
    occupation = "Software Developer"
    net_worth = 10,000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
print(a.name,a.occupation)
a.info()