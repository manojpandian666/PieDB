<h3>Specify your path in path variable as String</h3>

path ="PieDB/keys"

<strong>create(key,value,timetolive)</strong> -- value must be a JSON Object -- if timetolive not defined it will persist in db.
    creates a file with the specified key and value of the JSON

<strong>read(key)</strong>
    read a file with that key and returns as JSON object

<strong>update(key,new_vaue)</strong> -- value must be a JSON Object
    updates the file with new value

<strong>delete(key)</strong>
    deletes the file with that key

```python
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
