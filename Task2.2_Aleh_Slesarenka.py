print("Hi.Enter the word or number for test:")
string = input()


def check(string):
    if (string == string[::-1]):
        print("Yes, it is.")
    else:
        print("No,it isn't")


check(string)
