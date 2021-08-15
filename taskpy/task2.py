tuple3=("apple","orange",4,8.98,"jackfruit")
for x in tuple3:
    if x==8.98:
        break
        print("Printed tuple ")
    else:
        print("tuple not printed")
        print(x)
        tuple4=tuple3*2
        print(tuple4)
        tuple5=("happy",5,14.5,7,"happy",12,"true","happy")
        x=tuple5.count("happy")
        print(x)
        x=tuple5.index(14.5)
        print(x)
        
    
    