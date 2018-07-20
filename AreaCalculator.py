#p1 chooses, calculates and prints the area of a triangle or circle
print "Calculation starting..."
option= raw_input("Enter C for Circle or T for Triangle: ")
if option== "C":   
    radius= raw_input("enter radius")   
    radius = float(radius)  	
    p=3.14159  	
    area= p*radius**2  	
    print area  
elif option==  "T": 
    base = raw_input('what is base length')  	
    base = float(base)  	
    height = raw_input('input height here')  	
    height = float (height)  	
    area= 0.5*base*height  
    print area 
else:
  print "invalid"