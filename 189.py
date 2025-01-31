
#Open the file "demofile2.txt" and overwrite the content to the file ?

f = open("demofile.txt", "w")
f.write("Woops! i have deleted the content!")

f.close()

# open and read file after overwriting

f = open("demofile.txt", "r")
print(f.read())
f.close()