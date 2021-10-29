import time
import os


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
    print("Animals")
    choice = input()
    menu()


def addAnimal():
    os.system("cls")
    print("adding new animal")
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