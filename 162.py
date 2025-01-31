#Else

#You can use the else keyword to define a block of code to be executed
# if no errors were raised:

#In this example, the try block does not generate any error !

try:
    print("hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")