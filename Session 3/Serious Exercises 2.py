
sz = [5, 7, 300, 90, 24, 50, 75]

print()
print("hello, my name is Huong and these are my ship sizes: ",sz)      
print("after shearing",sz)
for n in range(4):
        print("month: " ,n)
        print ("now here is my fock: ",sz)
        sz.sort()
        a = sz[6]
        print("Now my biggest sheep has size", a, "let's shear it")
        sz[6] = 8
        print ("After shearing, here is my flock", sz)
        b= [50,50,50,50,50,50,50]
        sz= [sum(x) for x in zip(sz, b)]


print("my flock has size in total: ",sum(sz))
print("i would get: ",sum(sz)*2,"$")

##a = int(input("month = "))    
##for n in range (a):
##    
##        print("month =", n)
##        
##        sheep = [b + n * 50 for b in sz]
##        print("{0} month has passed, now here is my flock".format(n), sheep)
##        
##        c = max(sheep)      
##        print("Now my biggest sheep has size", c, "let's shear it")
##
##        d = sheep.index(c)
##        sheep.pop(d)
##        print("After shearing, here is my flock", sheep)
