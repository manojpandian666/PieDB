import PieDB as db


x = {"Name":"Manoj","Desgination":"Software Engineer"}
y = {"Name":"Manoj Pandian","Desgination":"Software Engineer"}

db.create("key002", x, 2)

db.create("key003", x)

db.create("key004",x)

x = db.read("key004")
print(x)

db.update("key004", y)

db.delete("key003")

