#This program find the number of devisors of an integer

import math

def divisor():
    no_divisor = []
    print ("This is a diviosr program")

    no = input("Enter the number")

    no_range = range(2,no)

    for i in no_range:
        if no % i == 0:
            no_divisor.append(i)
    return no_divisor

def main():
    a = divisor()
    for i in a:
        print "Devisors are",i  
    print(a)

if __name__ == "__main__":

    main()
