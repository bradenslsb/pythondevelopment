def remove_first_and_last(list_to_clean):
    new_list = []
    list_to_clean[2:-2] = new_list
    content = list_to_clean
    return content


code = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last(code))
def someDict (mydict):
    #return myDict = [dict([key, int(value)]


def returnSum(myDict): 
    sum = 0

    for i in myDict: 
        sum = sum + myDict[i] 
      
    return sum
  
# Driver Function 
dictionary = {'a': 100, 'b':"200", 'c':300} 
print("Sum :", returnSum(dictionary))
d={
'A':100,
'B':540,
'C':239
}


def dictionarySum (dictionary):
    mkndiction = [dictionary([key, int(value)])]

print(sum(d.values()))
class DifferentWebsite:
    title = "My Class Title"

dw = DifferentWebsite()
print(dw.__dict__)

dw_two = DifferentWebsite()
print(dw_two.__dict__)

class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f"Hi {self.first_name} {self.last_name}"

class AdminUser(User):
    def active_users(self):
        return "500"



tiffany = AdminUser("tiffany@devcamp.com", "Tiffany", "Hudgens") 
import math


def pretty_price(number, decimal):
    if number > 0:
        new_number = math.floor(number)
        "{:.2f}".format(new_number)
        return new_number + decimal

print(pretty_price(5.44, .77))
def reshape(number):
    integers_to_append = range(number + 1)
    sec_arr = [*integers_to_append]
    return sec_arr 

print(reshape(5))
    
    
def manual_incrementing_matrix(n):
    matrix = [ [ None for y in range(n) ] for x in range(n) ]

    counter = 0

    for idx, el in enumerate(matrix):
        for nested_idx, nested_el in enumerate(el):
            matrix[idx][nested_idx] = counter + nested_idx

        counter += 1

    return matrix

print(manual_incrementing_matrix(5)) 