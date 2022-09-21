# # grinning face
# print("\U0001f600")
#
# # grinning squinting face
# print("\U0001F606")
#
# # rolling on the floor laughing
# print("\U0001F642")


#-------------------------------------------lambda function-------------------------------------


# a=5
# b=7
#
# x= lambda a,b : a*b
# print(x(a,b))




#-------------------------------------------list-------------------------------------








# n= input("Enter a text of numbers: ")
#
# list = n.split()
#
# sum =0
# for x in list :
#     sum =sum + int(x)
#
# print(sum)


#-------------------------------------------matrix-------------------------------------

#
# matrix=[[1,2,4],[3,6,8]]
#
# for r in matrix:
#     for c in r:
#         print(c)






#-------------------------------------------dictionary-------------------------------------




#
# studentId ={
#     "101" : "Alif", #string was use so it is needed to use quatation marks in studentId while printing
#      102 : "Sayem", #int was use so no need to use quatation marks in studentId while printing
#     "103" : "Zawwad",
#     "104" : "Fahim",
# }
#
# print(studentId["101"])
# print(studentId.get("103")) #or
# print(studentId[102])
# print(studentId.get(106, "not exist in dictionary" )) #106 is not in studentId dictionary so it would show null in output. rather than printing null I used "not exist in dictionary"...




#-------------------------------------------Tuple-------------------------------------(for tuple we will use  first bracket rather than second bracket which was used in dictionary.




# students = (
#
#     "alif", "sayem", "zawwad",
#     ("rayed",8,5.57,) #touples inside touple
#
# )
#
# #students[0]=fahim #not possible. it will show errror. because tuple value can not be changed.
#
# print(students[0])
#
# print(students[3])
#
# print(students[3][1])



#-------------------------------------------Stack-------------------------------------(lifo) example: feather can


# books =[]
#
# books.append("learn c") #first added books
# books.append("learn c++")
# books.append("learn python") #last added books
#
# print(books)
#
# books.pop() #last book will be removed
# print(books)
# books.pop()
# books.pop()
#
#
# if not books:
#     print("No books left")




#-------------------------------------------Queue-------------------------------------(fifo) example: bank queue




# from collections import deque
#
# bank = deque(["alif", "fahim", "rayed"])
# print(bank)
# bank.popleft()
# print(bank)
#
# bank.popleft()
# bank.popleft()
# if not bank:
#     print("No person")






#-------------------------------------------Function-------------------------------------



# def my_function():
#     print("Its a function.")
#
#
# my_function()
#
#
# def my_function(fname):
#     print(fname+" plays football")
#
# my_function("fahim")
# my_function("alif")
# my_function("zawwad")
#
#
# def football_time_slot(fname, time):
#     print(fname, "plays football at", time )
#
# football_time_slot("alif", "5.30am")
# football_time_slot("fahim", "3.30pm")


# def total_kids_name(*kid): #if number of arguement is unknown add asterisk before arguement.
#     print("The youngest child is " , kid)
#
# def youngest_kid(*kid):
#     print("The youngest child is " , kid[2])
#
# total_kids_name("Emil", "Tobais", "Linus")
# youngest_kid("Emil", "Tobais", "Linus")



# def last_name(**person):   #This way the function will receive a dictionary of arguments
#     print("person's last name is", person["lname"])
#
# def first_name(**person):
#     print("person's last name is", person["fname"])
#
#
# last_name(fname="alif", mname="al", lname="razi")
#
# first_name(fname="alif", mname="al", lname="razi")




# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# def return_test(x):
#   return 5*x
#
#
# print(return_test(3))



# def myfunction_pass():     #function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
#   pass



# def recursion_test_factorial(n): #recursion
#   if(n<=1):
#     return 1
#   else:
#     return n*recursion_test_factorial(n-1)
#
# k=6
# print(recursion_test_factorial(k))




#-------------------------------------------formattted string----------------------------------

#
#
# num1=20
# num2=30
#
# print(f"{num1}+{num2}={num1+num2}")




#-------------------------------------------class object--------------------------------------------




# class student:
#   roll=""
#   gpa=""
#
#
# rahim=student()     #creating object
# print(isinstance(rahim,student))    #checking there is object, class or not
#
# rahim.roll =101
# rahim.gpa = 3.6
#
# karim= student()
#
# karim.roll=102
# karim.gpa=3.5
# print("rahim roll:", rahim.roll, " rahim gpa:", rahim.gpa)    #we printed this several times
# print(f"Roll: {rahim.roll}, gpa: {rahim.gpa}")  #or
#
# print("karim roll:", karim.roll, " karim gpa:", karim.gpa)     #we printed this several times
# print(f"Roll: {karim.roll}, gpa: {karim.gpa}")  #or





#-------------------------------------------method--------------------------------------------    in method we are creating a function which will print the funtion



# class student:
#   roll=""
#   gpa=""
#
#
#   def display(self):
#     print(f"Roll: {self.roll}, gpa: {self.gpa}")
#
#
# rahim=student()     #creating object
# print(isinstance(rahim,student))    #checking there is object, class or not
#
# rahim.roll =101
# rahim.gpa = 3.6
#
# karim= student()
#
# karim.roll=102
# karim.gpa=3.5
#
# rahim.display()
# karim.display()




#---------------------------------------------or(method)---------------------------------------




# class student:
#   roll=""
#   gpa=""
#
#
#
#
#   def set_value(self,roll, gpa):
#
#     self.gpa=gpa
#
#     self.roll=roll
#
#
#
#   def display(self):
#     print(f"Roll: {self.roll}, gpa: {self.gpa}")
#
#
# rahim=student()     #creating object
# #print(isinstance(rahim,student))    #checking there is object, class or not
#
#
#
# # rahim.roll =101
# # rahim.gpa = 3.6
#
# karim= student()
#
#
# rahim.set_value(101,3.6)
#
# karim.set_value(102,3.5)
#
# # karim.roll=102
# # karim.gpa=3.5
#
# rahim.display()
# karim.display()




#---------------------------------------------or(method)---------------------------------------




# class student:
#   roll=""
#   gpa=""
#
#
#
#
#   def set_value(self,roll, gpa):
#
#     self.gpa=gpa
#
#     self.roll=roll
#
#
#     print(f"Roll: {self.roll}, gpa: {self.gpa}")
#
#
#
#   # def display(self):
#   #   print(f"Roll: {self.roll}, gpa: {self.gpa}")
#
#
# rahim=student()     #creating object
# #print(isinstance(rahim,student))    #checking there is object, class or not
#
#
#
# # rahim.roll =101
# # rahim.gpa = 3.6
#
# karim= student()
#
#
# rahim.set_value(101,3.6)
#
# karim.set_value(102,3.5)
#
# # karim.roll=102
# # karim.gpa=3.5
#
# # rahim.display()
# # karim.display()




#---------------------------------------------constructor(__init__)(parameter in object)---------------------------------------


# class student:
#   roll=""
#   gpa=""
#
#
#
#
#   def __init__(self,roll, gpa):
#
#     self.gpa=gpa
#
#     self.roll=roll
#
#
#   def display(self):
#     print(f"Roll: {self.roll}, gpa: {self.gpa}")
#
#
# rahim=student(101,3.6)     #parameter in object
#
#
#
# karim= student(102,3.5)
#
# rahim.display()
# karim.display()







#---------------------------------------------exercise(class,object,method, constructor)---------------------------------------



# class triangle:
#   base=""
#   height=""
#
#   def __init__(self, base, height):
#     self.base=base
#     self.height=height
#
#   def calculate_area(self):
#     area = .5*self.base*self.height
#     print("area of the triangle:", area )
#
#
#
# t1= triangle(10,8)
# t1.calculate_area()
#
# t2= triangle(20,8)
# t2.calculate_area()







#---------------------------------------------inheritance---------------------------------------





# class phone:
#   def call(self):
#     print("you can call")
#
#   def message(self):
#     print("you can message")
#
#
# class samsung(phone):
#   def photo(self):
#     print("you can take photo")
#
#
#
#
# s = samsung()
# s.call()
# s.message()
# s.photo()
#
#



#---------------------------------------------override(same method in child class, so it need to override to print child class method)---------------------------------------




# class phone:
#   def __init__(self):
#     print("I am in phone class")
#
#
# class samsung(phone):
#   def __init__(self):
#     super().__init__()     #or super(samsung, self).__init__()
#     print("I am in samsung class")
#
#
#
# s= samsung()


#---------------------------------------------example inheritance---------------------------------------



# class shape:
#     def __init__(self, dim1, dim2):
#         self.dim1=dim1
#         self.dim2=dim2
#
#     def area(self):
#         print("I am the area method of shape class")
#
#
# class triangle(shape):
#     def area(self):
#         area = 0.5 * self.dim1 * self.dim2
#         print("Area of the triangle: ", area)
#
#
# class rectangle(shape):
#     def area(self):
#         area = self.dim1 * self.dim2
#         print("Area of the rectangle: ", area)
#
#
# tr1 = triangle(20,30)
# tr1.area()
# tr2 = triangle(20,10)
# tr2.area()
#
# rt1 = rectangle(40,50)
# rt1.area()
# rt2 = rectangle(35,20)
# rt2.area()





#---------------------------------------------FILE---------------------------------------





#file = open("student.txt","r+")  #r->read mode, w->write, r+  -> read+write
#
# #text= file.read()
# #size= len(text)
# #print(text)
#
# # text_line= file.readlines()[0] #printing 1st lines
# # print(text_line)
#
# for line in file: # printing each line using for loop
#     print(line)
#
#
#
#
#
# #print(file.readable()) #show true
#
#
# file.close





#write + append




# file = open("student.txt","a")
# file = open("student1.txt","w") #all will be removed in the file and wrie new things. if no file exist it will create new file.
#
#
#
# file.write("\nfsdjldksfsdkgdks")
#
# file.close()





#any file can be created






# file = open("hello.html","w")
#
# file.write("<h1> This is a text </h1>")
#
# file.close()



#---------------------------------------types of inheritance--------------------------------


# class a:
#     def display1(self):
#         print("i am in class a")
#
#
# class b(a):
#     #display1()
#     def display2(self):
#         print("i am in class b")
#
#
# class c(b):
#     # display1()
#     # display2()
#     def display3(self):
#         print("i am in class c")
#
#
# obj1= c()
#
# obj1.display1()
# obj1.display2()
# obj1.display3()



#multiple inheritance





# class a:
#     def display1(self):
#         print("i am in class a")
#
#
# class b:
#
#     def display2(self):
#         print("i am in class b")
#
#
# class c(a,b):
#     pass
#     # display1()
#     # display2()
#     # def display3(self):
#     #     print("i am in class c")
#
#
# obj1= c()
#
# obj1.display1()
# obj1.display2()
# # obj1.display3()







#------------------------------------abstract----------------------------





                                         #####
# from abc import ABC ,abstractmethod         #
#                                              #
#                                              #
# class shape(ABC):                            #
#     def __init__(self, dim1, dim2):           #
#         self.dim1=dim1                         #   abstraction
#         self.dim2=dim2                        #
#                                              #
#     @abstractmethod                          #
#     def area(self):                          #
#         pass                               #
#                                       ####
#
# class triangle(shape):
#     def area(self):
#         area = 0.5 * self.dim1 * self.dim2
#         print("Area of the triangle: ", area)
#
#
# class rectangle(shape):
#     def area(self):
#         area = self.dim1 * self.dim2
#         print("Area of the rectangle: ", area)
#
#
#
#
#
#
# tr1 = triangle(20,30)
# tr1.area()
# tr2 = triangle(20,10)
# tr2.area()
#
# rt1 = rectangle(40,50)
# rt1.area()
# rt2 = rectangle(35,20)
# rt2.area()
#
