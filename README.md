<h3>Specify your path in path variable as String</h3>

path ="PieDB/keys"

<strong>create(key,value)</strong> -- value must be a JSON Object
    creates a file with the specified key and value of the JSON

<strong>read(key)</strong>
    read a file with that key and returns as JSON object

<strong>update(key,new_vaue)</strong> -- value must be a JSON Object
    updates the file with new value

<strong>delete(key)</strong> 
    deletes the file with that key
