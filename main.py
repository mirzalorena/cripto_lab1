
#gcd with loops
def computeGcdLoops(a,b):
    if a>b:
        aux=b
    else:
        aux=a
    for i in range(1,aux+1):
        if (a%i==0) and (b%i==0):
            result=i
    return result

#gcd with recursion
def computeGcdRecursion(a,b):
    if(b==0):
        return a
    else:
        return computeGcdRecursion(b,a%b)

#gcd with euclidian algorithm
def computGcdEuclidian(a,b):
    while(b):
        a,b=b,a%b

    return a


if __name__ == '__main__':
    print("Hello")

    print("1. Gcd with Loops")
    print("2. Gcd with recursion")
    print("3. Gcd with Euclidian alogrithm")
    print("0. Exit")

    option=input("Choose a method: ")

    while (option != "0"):
        a=int(input("Give first number: "))
        b=int(input("Give second number: "))

        if(option=="1"):
            print(computeGcdLoops(a,b))
        elif(option=="2"):
            print(computeGcdRecursion(a,b))
        elif(option=="3"):
            print(computGcdEuclidian(a,b))


        option=input("Choose a method: ")




