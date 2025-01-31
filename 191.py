# create an txt file named work.txt?
# add 5 lines using write ?
# add 2 lines to end using append?
# print first 4 lines using readline()?
# overwrite using another 2 lines?
#last read all




f = open("work.txt", "x")

 = open("work.txt", "w")
#g.write("Woops! i have deleted the content! \n wohfohfojehjvhdio \n jhwjdhwjh9fuwhu9 \n  jhwhwjhifcwish \n  whjofhowhfi")


g.close()


f = open("work.txt", "a")
f.write("first append\n second append")



f = open("work.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())



f = open("work.txt", "w")
f.write("first line \n second line")
f.close()




f = open("work.txt", "r")
print(f.read())