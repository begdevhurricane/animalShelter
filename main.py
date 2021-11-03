import time
import os
import mysql.connector

# create connection with database
db = mysql.connector.connect(
    host="localhost",
    user="adrian",
    passwd="adrian",
    database="test"
    )

# In order to put our new connnection to good use we need to create a cursor object.
# It gives us the ability to have multiple seperate working environments through the same connection to the database.
# You can create a cursor by executing the 'cursor' function of your database object.

# create cursor object
cur = db.cursor()

# Create animals table
# cur.execute("CREATE TABLE animals (animalId int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), type VARCHAR(15), race VARCHAR(15), age smallint UNSIGNED )")


def menu():
    # show menu options
    os.system("cls")
    print("display animals: 1")
    print("add new animal: 2")
    print("delete animal: 3")
    print("edit animal: 4")
    print("\nwrite 'exit' to exit application")
    choice = input()

    # choose option
    if choice == '1': displayAnimals()
    if choice == '2': addAnimal()
    if choice == '3': deleteAnimal()
    if choice == '4': editAnimal()
    if choice == 'exit': exit()

    print("\nWrong option, try again...")
    time.sleep(3)
    menu()


def displayAnimals():
    os.system("cls")

    cur.execute("Select * FROM animals")
    for animal in cur:
        print(animal)

    choice = input()
    menu()


def addAnimal():
    os.system("cls")
    print("adding new animal: ")

    print("name: ")
    name = input()

    print("type: ")
    animalType = input()

    print("race: ")
    race = input()

    print("age: ")
    age = input()

    cur.execute("INSERT INTO ANIMALS (name, type, race, age) VALUES (%s, %s, %s, %s)", (name, animalType, race, age))

    choice = input()
    menu()


def deleteAnimal():
    os.system("cls")
    print("delete animal")
    choice = input()
    menu()


def editAnimal():
    os.system("cls")
    print("editing animal")
    choice = input()
    menu()


# start
print("Welcome to the animal shelter app\n")
menu()

# TODO
# make a verification function that can verify length of variables that we want to add into database
# It will prevent adding to long names etc.