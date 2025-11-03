def even(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")
even(5)
even(10)

def multiply(a, b):
    return a * b
print(multiply(10, 10))

def vowels(string):
    vowel = 0
    for i in range(len(string)):
        if string[i-1] in "aeiou":
            vowel = vowel + 1
        else:
            pass
    print("there are", vowel, "vowels in this string")
word = str("haha")
vowels(word)

def reverse(string):
    listnum = 1
    mylist = []
    list(string)[:]
    for items in (list(string)):
        mylist.append(list(string)[-listnum])
        listnum = listnum + 1
    reversed = "".join(mylist)
    print(reversed)
word1 = "dog"
reverse(word1)