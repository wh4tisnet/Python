mm=eval(input("Introduce un mes del año: "))
if mm==1 or mm==3 or mm==5 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12:
    print("31 dias")
if mm==4 or mm==6 or mm==9 or mm==11: 
    print("30 dias")
if mm==2:
    print("28/29 dias")
    