array = [{
    id: 1,
    'age': 15,
    'name': "Ikram"
}, {
    id: 2,
    'age': 18,
    'name': "Bob"
}, {
    id: 3,
    'age': 19,
    'name': "JoK"
}]

def getInfo(id_Number):
    for item in array:
        if item[id] == id_Number:
            return f"ID: {item[id]}\nName: {item['name']}\nAge {item['age']}"


print(getInfo(1))