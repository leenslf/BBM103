#Name= Leen Said
#Student no: 2220356194
def healthStatus(height,mass): #define the function
    BMI=mass/(height**2)
    if BMI>=30:  #create conditional statement
        print("Obese")
    elif BMI>=24.9:
        print("Overweight")
    elif BMI>=18.5:
        print("Healthy")
    else:
        print("Underweight")
