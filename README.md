Specify your path in path variable as String

path ="PieDB/keys"

create(key,value) -- value must be a JSON Object
    creates a file with the specified key and value of the JSON

read(key)
    read a file with that key and returns as JSON object

update(key,new_vaue) -- value must be a JSON Object
    updates the file with new value

delete(key) 
    deletes the file with that key