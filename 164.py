

try:
    f = open("demofile.txt")
    try:
        f.write("lorem ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")