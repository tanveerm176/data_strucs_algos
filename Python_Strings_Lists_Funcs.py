# Python Basics


def addtoX(x):
    print("HellloWorld")

    x = 5
    x = x + 5
    print(x)

    for i in range(x):  # range(x) == (0,1,2,3,4,x-1)
        i = i + 1
        print("i=", i)

    return i


# print(addtoX(6))


###############STRINGS#############################
#https://docs.python.org/3/library/string.html
def stringBasics():
    word = "Python is the best of the best"

    print("word[0:4]=", word[0:4])  # from position 0 (included)
    # to the letter at position 2 (excluded)

    print(
        "word[:2]=", word[:2]
    )  # from the start to the letter at position 2 (excluded)

    print("word[-1]=", word[-1])  # letter at last position

    print("word[-1:]=", word[-1:])  # from the letter at last position to end
    print("word[-3:]=", word[-3:])

    # built in functions
    print(len(word))

    word.capitalize()

    word.casefold()  # return casefold copy of str, Casefolded strings may be used for caseless matching
    # any non english letters to their english equiv
    #'ß' == 'ss'

    print("word.count('the')=", word.count("the"))

    print(
        "word.find('the')=", word.find("the")
    )  # returns the first index of the substring found, -1 if nothing
    print(
        "word.index('the')=", word.index("the")
    )  # same as above but raises ValueError when not found

    print("the" in word)  # returns boolean if substr found in str

    # String reformatting
    print("the sum of 1+2 is {0}".format(1 + 2))
    # the sum of 1+2 is 3

    # checking alphanumeric
    print("word.isalnum()=", word.isalnum())
    # return True if all chars in string are alpha AND num and there is atleast one character
    # True only when satisfy: word.isalpha(), word.isdecimal(), word.isdigit(), word.isnumeric()

    word.isupper()
    word.istitle()

    print(" AND ".join([word, word]))

    # lstrip(), removes all leading chars, defaults to whitespace if empty
    print(word.lstrip("Py"))  # thon is the best of the best
    print(word.strip())  # strips both l and r

    print("word.title()=", word.title())

    #    line = ' '.join(number_word_list[1:])
    # number_word_list = line.strip().split(" ")

def zipExample():
    #returns a tuple iterable from two iterables, combining them via index
    l1 = [1,2,3]
    l2 = ['a','b','c']

    zippedL1_L2 = zip(l1,l2) #[(1, 'a'), (2, 'b'), (3, 'c')]
    print(list(zippedL1_L2))

zipExample()


###############LISTS#############################
# https://docs.python.org/3/tutorial/introduction.html#text


def listBasics():
    squares = [1, 4, 9, 16, 25]
    print(squares)

    print(squares[0])
    print(squares[-3:])  # returns a new list
    print(squares + squares)


def fibo(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

# fibo(200)


def flowControl():
    wordList = ["cat", "window", "defenestrate"]
    for word in wordList:
        print(word)

    for word, index in enumerate(wordList):
        print("index=", index)
        print("word=", word)

    users = {"Hans": "active", "Elaine": "inactive", "Henry": "active"}
    print(users)

    print("users copy items=", users.copy().items())

    for user, status in users.copy().items():
        if status == "inactive":
            del users[user]

    print(users)


def iterRanges_break():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, "equals", x, "*", n // x)
                break
        else:
            print(n, "is a prime number")
    # 2 is a prime number
    # 3 is a prime number
    # 4 equals 2 * 2
    # 5 is a prime number
    # 6 equals 2 * 3
    # 7 is a prime number
    # 8 equals 2 * 4
    # 9 equals 3 * 3


def iterRanges_continue():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even num", num)
            continue
        print("Found an odd number", num)

    # Found an even num 2
    # Found an odd number 3
    # Found an even num 4
    # Found an odd number 5
    # Found an even num 6
    # Found an odd number 7
    # Found an even num 8
    # Found an odd number 9

# iterRanges_continue()
        
def matching(status):
    #only the first match gets executed
    match status:
        case 400:
            return "bad"
        case 404:
            return "not found"
        case 419:
            return "teapot"
        case 401 | 403 | 408:
            return "not allowed"
        case _:
            return "broken" # _ acts as a wildcard and never fails to match

def tuple_matching(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
    
# print(tuple_matching((5,6)))

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# ask_ok('Do you really want to quit?')
        