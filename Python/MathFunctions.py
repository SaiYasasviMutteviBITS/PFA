def BMI (height,weight):

    bmi = weight / (height/100)**2  

    if bmi <= 18.5:  
        return (f"Your Body Mass Index is {bmi} You are underweight.")  
    elif bmi <= 24.9:  
        return (f"Your Body Mass Index is {bmi} You are healthy.")  
    elif bmi <= 29.9:  
        return (f"Your Body Mass Index is {bmi} You are over weight.")  
    else:  
        return (f"Your Body Mass Index is {bmi} You are obese.")




def nCr(n, r):
 
    return (fact(n) / (fact(r)
                * fact(n - r)))
 
# Returns factorial of n
def fact(n):
    if n == 0:
        return 1
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res