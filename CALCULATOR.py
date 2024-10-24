print('\n')

     
print('\t','\t',"C  A  L  C  U  L  A  T  O  R")


print('\n')

first= int(input("                  enter the first no.  "))
print('\n')
operator= input("                   enter the operator  ")
print('\n')
second= int(input("                 enter the second no.  "))

if operator == "*":
    print('\t')
    print('\t')
    print('\t')
    print("                          ",first, "X" , second, "=", first*second)
elif operator=="+":
   print('\t')
   print('\t')
   print('\t')
   print("                       ",first, "+" , second, "=", first+second)
elif operator=="-":
    print('\t')
    print('\t')
    print('\t')
    print("                       ",first, "-" , second, "=", first-second)
elif operator=="/":
    print('\t')
    print('\t')
    print('\t')
    print("                      ",first, "/" , second, "=", first/second)
else:
    print('\n')
    print('\n')
    print('\n')
    print("mind your logic and verify the operation....")
