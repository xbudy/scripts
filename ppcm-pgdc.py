nb1 = int(input("enter nb1 ; "))
nb2 = int(input("enter nb2 ; "))


def getFactors(n):
    # Create an empty list for factors
    factors=[];

    # Loop over all factors
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    # Return the list of factors
    return factors

# Call the function with a given value
nb1f=getFactors((int(nb1)))
nb2f=getFactors((int(nb2)))
#print ("nb1 divs ",nb1f,"and nb2 divs ",nb2f)
divc= [x for x in nb1f if x in nb2f ]
print ("hhhh nadee pgdc ==> ",max(divc))
if nb1>nb2 :
  pg=nb1
else :
  pg=nb2
i=nb1*nb2
while i >= pg :
  if i%nb1==0 and i%nb2==0:
    m=i
  i=i-1
  
print("ppcm. ", m)
    
  
  
