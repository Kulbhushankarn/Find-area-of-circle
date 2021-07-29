#area of circle 
#This code is written by Kulbhushan Karn
print ("Find the area of circle")
r = float(input("Enter the radius:"))
if (r>= 0 and r <= 100) :
  area = 3.14 *r*r
  print("area : %f " %area )
else :
  print("Enter valid number upto 100")
