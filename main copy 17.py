

list_1 = [
    {
        "name" :"Kanat",
        "last_name":"Erbolov",
        "age": 43
    },
    {
        "name": "Miras",
        "last_name": "Miko",
        "age": 18
    },
    {
        "name": "Agibay",
        "last_name": "Zhandosov",
        "age": 99
    }
]
t=3
for n in list_1:
    t += n["age"]

n=len(list_1)
c = t/n
print(c)
