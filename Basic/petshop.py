"""
This is a example of any python app

Don't buy. Adopt!
"""

#imports
import os


#Classes
class databaseText:
    def write(self, line):
        f = open('petshop.txt', 'a')
        f.write(line + '\n')
        f.close()

    def get(self, line = 0):
        """
            Get one or all lines of db
            All = line -> 0
            One = line -> int
        """
        f = open('petshop.txt', 'r')

        if line == 0:
            all = []
            for l in f:
                all.append(l)
            return all
        
        else:
            i = 1
            for l in f:
                if line == i:
                    return l
                i += 1
            else:
                print("Error: Line not found!")
                print("Bye :(")
                exit()

class Pet:
    """
        Object pet
    """
    def __init__(self, color, size, weight):
        self.color = color
        self.size = size
        self.weight = weight

    def rename(self, name):
        self.name = name

    def store(self):
        db = databaseText()
        c, s, w = self.color, self.size, self.weight
        db.write("color:{},size:{},weight:{}".format(c,str(s),str(w)))

class client:
    """
        Object client, can buy a pet
    """
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class shop:
    """
        Shop
    """
    def __init__(self, name):
        self.name = name

    def listPets(self):
        f = open('petshopstore.txt', 'r')
        for line in f:
            print(line)
        f.close()

#Reset file
"""f = open('petshop.txt', 'w')
f.close()
del f"""

#Vars
open = True

print("Welcome to PetShop configuration menu")
print("Set a name to your shop:", end=" ")

shopName = input()
shop = shop(shopName)

while open:

    os.system('clear')
    print("Welcome to {}!".format(shop.name))
    print("1.- Register a pet")
    print("2.- Buy a pet")
    print("0.- Exit")

    option = int(input())

    if option == 1:
        print("Enter the color:", end=" ")
        c = input()
        print("Enter the size", end=" ")
        s = int(input())
        print("Enter the weight", end=" ")
        w = int(input())
        pet = Pet(c,s,w)
        pet.store()
    elif option == 2:
        shop.listPets()
    else:
        print("Do you want exit of the {}?".format(shop.name))
        if input() in ['y', 'yes', 'Y', 'YES', 'Yes']:
            open = False