print("---------------")
print("*** Bunyols ***")
print("---------------")
Bvacio=eval(input("Quants bunyols buits vols?: "))
Bcarabassa=eval(input("Quants bunyols de carabassa vols?: "))
if Bvacio<0:
    print("No pots introduir numeros negatius")
elif Bcarabassa<0:
    print("No pots introduir numeros negatius")
if Bvacio>=10 and Bcarabassa>=10:
     Bvacio=Bvacio*0.50-1
     Bcarabassa=Bcarabassa*0.75-1
     precioT=Bcarabassa+Bvacio
     print("Son",precioT,"€")
     pago=eval(input("Quants diners entrega?: "))
     vulta=precioT-pago
     if precioT>pago:
         vuelta2=precioT-pago
         print("Et falten",vuelta2,"€")
     elif(precioT==pago or precioT<pago):
         vuelta3=pago-precioT
         print("La volta es de:",vuelta3,"€")
elif Bvacio>0 and Bcarabassa>=0:
    Bvacio=Bvacio*0.50
    Bcarabassa=Bcarabassa*0.75
    precioT=Bvacio+Bcarabassa
    print("Son",precioT,"€")
    pago=eval(input("Quants diners entrega?: "))
    vulta=precioT-pago
if precioT>pago:
    vuelta2=precioT-pago
    print("Et falten",vuelta2,"€")
elif(precioT==pago or precioT<pago):
    vuelta3=pago-precioT
    print("La volta es de:",vuelta3,"€")