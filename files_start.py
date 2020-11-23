def main():
    #f = open("textfile.txt", "w+")
    f = open("textfile.txt", "w+")

    for i in range(10):
        f.write("This is a line " + str(i) + "\r\n")

    if f.mode == 'r':
        # contents = f.read()
        fl = f.readlines()

        for x in fl:
            print(x)


if __name__ == '__main__':
    main()