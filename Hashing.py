class hashTable:

    def __init__(self):                              # constructor

        self.size = int(input("Enter the Size of the hash table : "))
        self.table = list(None for i in range(self.size))
        self.collection ={}
        self.elementCount = 0
        for i in range(self.size):
            name = input("Enter name: ")
            ele = int(input("Enter Number: "))
            self.collection[name] = ele
    
    def prime(self):
        prime_l = []
        for i in range(2,self.size):
            for j in range(2,i):
                if i%j == 0:
                    break
                elif j == (i-1):
                    prime_l += [i]

                else:
                    pass
        
        return max(prime_l)



    def isFull(self):
        
        if self.elementCount == self.size:
            return True
        else:
            return False
    
    def hashFn2(self,key):
        return (self.prime() - key%self.prime())

    def hashFunction(self, element):                

        return element % self.size   #  it returns the index of element

    def insert(self):
        print("Which method ?")
        print("1. Linear Probing")
        print("2. Double Hashing")
        ask = int(input("Enter choice:"))

        if self.isFull():
            print("Hash Table Full")
            return False
        
        elif ask == 1 :
            self.linear_prob()
        else:
            self.double_hashing()

    def linear_prob(self):
        for i in self.collection:
            ele = self.collection[i]
            
            index = self.hashFunction(ele)

            if self.table[index] is  None:      #no collision
                self.table[index] = i
                self.elementCount += 1

            else:                               # collision
                index += 1
                while True:
                    if index >= self.size:
                        index = 0

                    if self.table[index] is None:
                        self.table[index] = i
                        self.elementCount += 1
                        break
                    else:
                        index += 1

    def double_hashing(self):
        for j in self.collection:
            i = 0
            ele = self.collection[j]
            while True:                           # collision
                index = (self.hashFunction(ele) + i*(self.hashFn2(ele)))%self.size
                if index >= self.size:
                    index = 0

                if self.table[index] is None:
                    self.table[index] = j
                    self.elementCount += 1
                    break
                else:
                    i += 1

    def display(self):

        print("\n")
        print("Size of Hash Table = ",self.size)
        print("Prime number chosen = ",self.prime())

        for i in range(self.size):
            ele = self.table[i]
            print("Hash Value: " + str(i) +"\t\t" + str(ele) +"\t" +"Phone No: "+"\t"+str(self.collection[ele]))
        

        print("The number of phonebook records in the Table are : " + str(self.elementCount))

choice1 = 0
while (True):
    print("****")
    print("1. Hashing      *")
    print("2. Exit                *")
    print("****")

    choice1 = int(input("Enter Choice: "))

    if choice1 == 1:
        h1 = hashTable()
        choice2 = 0
        while (True):
            print("****")
            print("1. Insert              *")
            print("2. Display             *")
            print("3. Back                *")
            print("****")

            choice2 = int(input("Enter Choice: "))

            if (choice2 == 1):
                h1.insert()

            elif (choice2 == 2):
                h1.display()
            else:
                break
    elif choice1 == 2:
        break




