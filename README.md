<h3>Specify your path in path variable as String</h3>

path ="PieDB/keys"

<span style="color: green"><strong>create(key,value,timetolive)</strong></span> -- value must be a JSON Object -- if timetolive not defined it will persist in db.
    creates a file with the specified key and value of the JSON

<span style="color: green"><strong>read(key)</strong></span>
    read a file with that key and returns as JSON object

<span style="color: green"><strong>update(key,new_vaue)</strong></span> -- value must be a JSON Object
    updates the file with new value

<span style="color: green"><strong>delete(key)</strong></span>
    deletes the file with that key
```
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
```
