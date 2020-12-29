<h1>PieDB - A simple file based Key Value data store.</h1>

<h3><u>Specify your storage path in path variable as String</u></h3>
path ="PieDB/keys"


<h3><u>Functions of data store</u></h3>

<h3>Functions of data store</h3>

<strong>create(key, value, timetolive)</strong>  -- value must be a JSON Object -- if timetolive not defined it will persist in db.
    creates a file with the specified key and value of the JSON

<strong>read(key)</strong>
    read a file with that key and returns as JSON object

<strong>update(key, new_vaue)</strong> -- value must be a JSON Object
    updates the file with new value

<strong>delete(key)</strong>
    deletes the file with that key


```python
import PieDB as db


x = {"Name":"Manoj","Desgination":"Software Engineer"} # JSON Object
y = {"Name":"Manoj Pandian","Desgination":"Software Engineer"} # JSON Object

db.create("key002", x, 2) # Creates a file with that key --- create(key, value, timetolive)

db.create("key003", x)

db.create("key004",x)

x = db.read("key004") # Returns the JSON Object
print(x)

db.update("key004", y) # Updates the value with that key

db.delete("key003") # Deletes the value with that key
```
