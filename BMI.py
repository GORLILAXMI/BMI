try:
    weight=float(input("enter your weight in kilograms:"))
    height=float(input("enter your height in meters:"))
    BMI=weight/(height**2)
    def cal(BMI):
        if BMI <18.5:
                     return "Under Weight" 
        elif 18.5 <= BMI < 24.9:
            return " Normal Weight"
        elif 25<= BMI < 29.9:
            return "Over Weight"
        else:
           return "Obesity"
    result=cal(BMI)
    print("YOUR BMI IS ",BMI)
    print("YOU ARE UNDER THE CATEGORY",result)

except ValueError:
    print("please enter a valid input")
        
    
    
    
