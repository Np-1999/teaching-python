class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def increase_age(self):
       # return self.age +1
       self.age = self.age + 1

class JDBC_Connection:
    def __init__(self, url, username, password, port):
        self.url = url
        self.username = username
        self.password = password
    def connect(self):
        self.url
    def disconnect(self):
        self.url

jdbc_connection1= JDBC_Connection(with arg set 1)
jdbc_connection2 = JDBC_Connection(with arg set 2)


jdbc_connection1.connect()
jdbc_connection2.connect()

nikhil = Person("Nikhil",27)
amar = Person("Amar","28")

print(nikhil.age)
print(amar.age)
nikhil.increase_age()
print(nikhil.age)