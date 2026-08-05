import random
print('Welcome To Wibyte Bakery!')
print('Here,You Get All Sorts Of Items,Even Rare Ones!')
menu=['Milkshake   ','Ice Cream   ','Choco Pie   ','Cookies     ','Paneer Pizza']
price=[39.99,15.00,49.99,25.00,239.99]
spl_menu = ["Chocolate Frogs","Fruit Tart","Blueberry Cheesecake","Bakalava","Onigiri","Mousse","O'cean Juice"]
spl_itemprc=[199.00,180.99,200.99,260.99,369.99,129.99,150.99]
spcl_idx = random.randint(0,7)
inventory=[]
menu.append(spl_menu[spcl_idx])
price.append(spl_itemprc[spcl_idx])
inventory.append(20)
print("This is Today's Menu")
print('ITEM','PRICE(INR)excl.tax',sep='\t\t\t')
for kk in range(len(menu)):
  print(str(kk+1)+"."+ menu[kk],price[kk],sep='\t\t')
  kk=kk+1
shoppingcomplete=0
s_c=[]
s_q=[]
while shoppingcomplete==0:
  order=int(input('Please tell me a Number between 1 and '+str(len(menu))+" for items,"+str(len(menu)+1)+'for bill \n'))
  if order<=len(menu) and order>0:
    print('Still shopping...')
    print('You Selected',menu[order-1])
    quant=int(input('How many units do you want to buy?\n'))
    if quant>0:        
        if menu[order-1]in s_c:
            print('repeated order')
            idx=s_c.index(menu[order-1])
            s_q[idx]=s_q[idx]+quant
        else:
            print('new selection')
            s_c.append(menu[order-1])
            s_q.append(quant)
    if quant<0:
        if menu[order-1]in s_c:
            print('repeated order')
            idx=s_c.index(menu[order-1])
            r_qty=min(abs(quant),s_q[idx])
            s_q[idx]=s_q[idx]-r_qty
            if s_q[idx]==0:
               del s_c[idx]
               del s_q[idx]
  elif order==len(menu)+1:
    print('Proceed to checkout,please take the 3rd right and 8th left...')
    shoppingcomplete=1
  else:
    print('Invalid Input')
gr_tot=0
print('Shopping Done,Displaying Shopping Cart')
print('ITEM   ','QUANT','UNIT PRICE  ','TOTAL PRICE',sep='\t\t\t,\b\b\b')
for kk in range(len(s_c)):
  idx=menu.index(s_c[kk])
  print('idx',idx)
  unitprice=price[idx]
  totalprice=unitprice*s_q[kk]
  tpr=round(totalprice,2)
  print(s_c[kk],s_q[kk],unitprice,tpr,sep='\t\t\t')
  gr_tot += tpr
print("Your grand total is",round(gr_tot,2),"Rupees")

dctlist = [10.0,20.0,30.0]
kk=1
nxtmullist=[]

for jj in range(len(dctlist)):
   dct_rate=dctlist[jj]
   searching=True
   kk=1
   while searching:
      nxtmul=500*(gr_tot//500.0+kk)
      gap500=round(nxtmul-gr_tot,2) 
      dct=nxtmul*dct_rate/100
      if gap500>dct:
        searching=False
      else:kk=kk+1
      nxtmullist.append(nxtmul)

for kk in range(1,len(nxtmullist)):
   if nxtmullist[kk]<=nxtmullist[kk-1]:
      nxtmullist[kk]=nxtmullist[kk-1]+500

print('We Have Some Offers For You!!!')
for kk in range (len(dctlist)):
   print(str(kk+1),".","Purcase for (INR) ",nxtmullist[kk]," to get a ",dctlist[kk],"% discount")
print('If you buy for '+ str(nxtmul)+'rupees,you get a 10%. discount')
print("You need to buy for "+str(gap500)+" to get the discount!")
w=int(input('Do You want to take this offer(1/2/3)'))
add_quant=[]
if w==1 or w==2 or w==3:
  gap500=nxtmullist[w-1]-gr_tot
  dct_rate=dctlist[w-1]
  print('You have Taken this offer!')
  print('You have the following options\n')
  for kk in range(len(menu)):
        add_quant.append((int(gap500//price[kk]+1)))
        print(str(kk+1), '. Add', menu[kk], str(add_quant[kk]), 'units')
  addon=int(input('Please indicate your preference\n'))
  if menu[addon-1]in s_c:
    print('repeated order')
    idx=s_c.index(menu[order-1])
    s_q[idx]=s_q[idx]+add_quant[addon-1]
  else:
    print('new selection')
    s_c.append(menu[addon-1])
    s_q.append(add_quant[addon-1])
else:
 print('Please pay '+str(gr_tot)+' Rupees(₹)')
 dct_rate=0.0
gr_tot=0.0
print('Shopping Done,Displaying Shopping Cart')
print('ITEM   ','QUANT','UNIT PRICE  ','TOTAL PRICE',sep='\t\t\t,\b\b\b')
for kk in range(len(s_c)):
  idx=menu.index(s_c[kk])
  print('idx',idx)
  unitprice=price[idx]
  totalprice=unitprice*s_q[kk]
  tpr=round(totalprice,2)
  print(s_c[kk],s_q[kk],unitprice,tpr,sep='\t\t\t')
  gr_tot += tpr
print("Your grand total is",round(gr_tot,2),"Rupees")
#dct_rate = 10.0; 
tax_rate = 10.0;

discount = round(dct_rate/100.0*gr_tot, 2)
tax = round(tax_rate/100.0*(gr_tot-discount), 2)

print('Your total order is (INR)', gr_tot)
print('Your order value, after discount is (INR)', round(gr_tot-discount, 2))
print('Tax (10%) is (INR)', round(tax, 2)); 
print('Total you have to pay (INR) ', round(gr_tot - discount + tax, 2))


print('Thanks')
print('Bye')



