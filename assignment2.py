# Demonstrate the use of all types of operators.
# 1) Arithmetic operators - (+,-,*,/,%,**,//)  

a = float(input("Enter number 1 : "))
b = float(input("Enter number 2 : "))
print("+ ",a+b)
print("- ",a-b)
print("* ",a*b)
print("/ ",a/b)
print("% ",a%b)
print("** ",a**b)
print("// ",a//b)

# 2) Assignment operators - (=,+=,-=,*=,/=,%=,//=,**=)

a += b
print("+= ",a)
a-=b
print("-= ",a)
a*=b
print("*= ",a)
a/=b
print("/= ",a)
a%=b
print("%= ",a)
a**=b
print("**= ",a)
a//=b
print("//= ",a)

# 3) Comparison operators - (== ,!= ,> ,< ,>= ,<=)

print("== ",a==b)
print("!= ",a!=b)
print("> ",a>b)
print("< ",a<b)
print(">= ",a>=b)
print("<= ",a<=b)

# 4) Logical operators (and ,or , not)

print("and ",a < 50 and  b < 100)
print("or ",a==b or a < 100)
print("not ",not(a==b))

# 5) Identity operators (is, is not)

print("is ",a is b)
print("is not ", a is not b)

# 6) Membership operators (in, not in)

l = list(range(1,101))
print("in ",a in l)
print("not in ",a not in l)
    
# 7) Bitwise operators (| ,& ,^ ,>> ,<<)
a = 110
b = 113
print("| ",a | b)
print("& ",a & b)
print("^ ",a ^ b)
print(">> ",a >> b)
print("<< ",a << b)