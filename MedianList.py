import statistics 
a = []
size = int(input("Enter The Size Of The List:"))
for i in range(size):
    val = int(input("Enter The Value:"))
    a.append(val)
print("Unordered List:", a)
a.sort()
print("Ordered List:", a)

def median(a):
        if (len(a)%2 != 0):
            middle=a[len(a//2)]
            print("Median Of This List Is:",middle)

        else:
            if (len(a)%2 == 0):
                first_middle=a[len(a//2)]
                second_middle=a[len(a//3)]
                result=first_middle/ second_middle
                print
            median(a)
            
                    
        
