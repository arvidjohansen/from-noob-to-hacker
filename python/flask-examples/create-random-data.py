import random


names = ["Arvid","Jonas","Jonathan","Petter"]
lastnames = ["Johansen","Skjelberg","Gravlaks","Tennisen"]
titles = ["Sjef","Markedsarbeider","Kontoransatt"]

res = []


for i in range(10):
    person = {}
    person["firstName"] = random.choice(names)
    person["lastName"] = random.choice(lastnames)
    person["title"] = random.choice(titles)
    person["age"] = random.randint(18,80)
    res.append(person)

print(res)