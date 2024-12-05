# try:                                #try key word is used to catch exceptions in the code here for example if the file tile.txt does not exist then the exection is catched and except block is executed
#     file = open("tile.txt")
#     a = {"hey":"jude"}
#     print(a["jude"])

# except FileNotFoundError:                   #once the exception is caught the code under the except block is executed also here FileNotFoundError is raised and caught but not the KeyError is raised
#     file=open("tile.txt", "w")
#     file.write("something")

# except KeyError as error_mes:               #here if the KeyError raised the following code is executed here "error_mes" is used to catch the error message and print it
#     print(f"key not found {error_mes}")

# else:
#     print(file.read())                      #else block is executed if no exception is raised


# finally:                                    #finally block is executed no matter what even if the exception is raised or not raised
#     file.close()
#     print("COMPLETED!")


# height = float(input("Enter the height of the person:"))

# if height > 3:
#     raise ValueError("Human cant be taller than 3meters")    # the raise keyword is used to create and catch your own error or exception 

# weight = int(input("Enter the weight of the person:"))



# bmi = weight / height ** 2 

# print(bmi)


dik = { "Amazon":{
                "email":"shubhambelbase2011@gmail.com",
                "password":"shub@123",
},

    "Facebook":{
                "email":"facebook@gmail.com",
                "password":"facebook@123",
},
}

import json
 
with open("D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY 29/storage.json", "r") as file:
    data = json.load(file)


for x,y in data.items():
    if x == "Facebook":
        message = "" 
        for obj in y:
            
            message = message + f"{obj}: {y[obj]}\n"

print(message)






