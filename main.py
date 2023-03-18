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
}, {
    id: 4,
    'age': 29,
    'name': "oLoa"
}, {
    id: 5,
    'age': 19,
    'name': "KOK"
}, {
    id: 6,
    'age': 69,
    'name': "JlK"
}]
maximum = int(len(array))
minimum = 1

def getInfo(x = minimum, y=maximum):
    result = array[x-1:y]
    storage = ""
    for item in result:
         storage += f"ID: {item[id]}\nName: {item['name']}\nAge: {item['age']}\n"
    return storage

print(getInfo(1, 5))