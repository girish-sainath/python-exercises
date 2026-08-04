def listChanger(list):
  print("Inner List :",list)
  list = ["Mango", "Kiwi", "Apple"]
  print("Changed List :",list)

fruits = ["Melon", "Orange", "Cherry"]

listChanger(fruits)
print("Original List :", fruits)

def addLemon(list):
  list.append("Lemon")
  print("Inner List :",list)

fruits = ['Melon', 'Orange', 'Cherry']
addLemon(fruits)

print("Original List:", fruits)