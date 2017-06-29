from random import randint

#functions
def level2(numlist):
    numSum = 0
    for num in numlist:
        if num % 5 == 0 or num % 3 == 0: #number is either a muliple of 5 or 3
            numSum += num
            
    print("Final sum:")
    print(numSum)
    


#running code
randomlist = []
for x in range (100):
     randnumber = randint(10,99)
     randomlist.append(randnumber)

 level2(randomlist)

#level3

def level3 (numlist):
    primeSum = 0

    #part1: iteratr=e through the list
    for num in numlist:

        prime = True

        #part2: determine if a prime number
        for x in range (2,num):
            if num % x == 0:
                prime = False

            if prime == True:
                print(num)
                primeSum += num

    #part3: add to the sum
    print("Final number")
    print(primesum)
