# Python has a built-in package called json which can be used to work with JSON data
import json 

x = '{ "name":"john", "age":30, "city":"New York"}'
y = json.loads(x)

print(y["age"]


#If you have a Python object then you can convert it into a JSON string using the json.dumps() method.
import json
x = {
    "name": "john",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)

print(y
