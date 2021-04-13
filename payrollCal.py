'''
    Harris Toe
    ENTD200 1003 Spr19
    Abaza, Ahmed
    Week  4 
    June 10, 2019
'''
'''
a = hourly rate
b = hours worked
'''
print("\n")
print("sampleCalculator\n")
userName= input("Please enter your name:")
while True:
  
    print("Welcome," + userName)
    #capture user inputs {input}
    hourly_Rate= input("Enter hourly Rate:")
    hours_worked=input("Enter hours worked:")
    overTime=input("Enter Overtime worked:")
    
    hourly_Rate=float(hourly_Rate)
    hours_worked=float(hours_worked)
    overTime=float(overTime)
    total=hourly_Rate*hours_worked
    print("total of", hourly_Rate,"*" , hours_worked,"*", overTime*1.5, "=", total)
    ans=input(userName + "Do you Want more calculation?(y/n)")
    if(ans=="y"):
        continue
    else:
        break
    
    print("Thank you for your hard work!")

