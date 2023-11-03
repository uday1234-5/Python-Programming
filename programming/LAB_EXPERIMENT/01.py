# INPUT SECTION
p = float(input("Enter the Principle Amount: "))
r = float(input("Enter the Rate of Monthy Interest: "))
n = float(input("Enter the Loan Term(in years): "))

# LOGIC SECTION
R = (r/12)/100 #Monthly Interest Rate
N = n*12
M = (p*R*((1+R)**N))/(((1+R)**N)-1)

#OUTPUT SECTION
print("\n")
print("Monthly Payment(in $) is: ", M)


