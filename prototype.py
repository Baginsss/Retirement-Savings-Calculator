#prototype of a program to calculate accumulation of savings for retirement

#variables
w = int(input("Age: "))
p = str(input("Gender: "))
k = int(input("Monthly Savings: "))
b2b = str(input("Status of Self-employment(yes/no): "))

#constants
l_ike = float(23472) 
l_ikze = float(9388.80) 
l_ikzeb2b = float(14083.20)
l_oipe = float(23472)

m_dage = float(73.4 - 60) #average life expectancy for men
f_dage = float(81.1 - 60) #average life expectancy for women

#operations
n = 60 - w #how many years to retirement

x = 12 * k #annual savings
x1 = x 

l = l_ike + l_ikze + l_oipe
l_b2b = l_ike + l_ikzeb2b + l_oipe

if b2b == "yes":
    if l_b2b < x:
        x = l_b2b
else:
    if l < x:
        x = l

def eme(x, n):
    for i in range(n):
        temp = (x * 1.07)+x1
        x = temp
    return round(x, 2)

def capital(x, n):
    for i in range(n):
        temp = x + x1
        x = temp
    return round(x, 2)

def retirement(x, p):
    if p == "m":
        return round((x / m_dage / 12), 2)
    else:
        return round((x / f_dage / 12), 2)

#Results
print("Savings for retirement: ", eme(x, n))
print("Accumulated capital: ", capital(x, n))
print("Monthly pension: ", retirement(eme(x, n), p))
