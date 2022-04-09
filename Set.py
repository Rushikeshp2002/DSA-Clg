s1 = set()

s1.add(10)

s1 = set(eval(input("Add your elements here: " )))

print(s1)

def add():
    n = int(input("Add the element here: "))
    s1.add(n)
    print(s1)

def remove():
    n = int(input("Add the element here to be removed: "))
    s1.remove(n)
    print(s1)

def add_sets():
    s2 = set(eval(input("Add set1 elements here: ")))
    
    s3 = set(eval(input("Add set2 elements here: ")))
    
    un = s2.union(s3)

    print(s2," + ",s3," = ",un)

def substr_sets():
    s2 = set(eval(input("Add set1 elements here: ")))

    s3 = set(eval(input("Add set2 elements here: ")))
    
    sub = s2 - s3

    print(s2," - ",s3," = ",sub)


def subset():
    s2 = set(eval(input("Add your elements here: ")))

    for i in s2:
        if i in s1:
            temp = 1
        else:
            temp = 0
            print(s2," is not a subset of ",s1)
            break
    if temp == 1:
        print(s2," is a subset of ",s1)


#main
while True:
        
    print("""1. To add new element
    2. To remove an element
    3. To add a two sets
    4. To substract two set
    5. To check for subset
    6. To print current set
    7. To exit""")

    ask = int(input("Enter your choice : "))

    if ask == 1:
        add()
    elif ask ==2:
        remove()
    elif ask == 3:
        add_sets()
    elif ask == 4:
        substr_sets()
    elif ask == 5:
        subset()
    elif ask == 6:
        print(s1)
    else:
        break
