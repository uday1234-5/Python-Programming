class Person:
    name = "Uday"
    age = 18
    university = "GLA University"
a = Person()
b = Person()
c = Person()

c.name = "om"
c.age = 15
c.university = "LPU University"
print(c.age,c.name,c.university)     ## print(Person().age)

b.name = "Kamal"
b.age = 20
b.university = "Dr. BPS College ."
print(b.age,b.name,b.university)     ## print(Person().age)
print(a.age,a.name,a.university)     ## print(Person().age)
