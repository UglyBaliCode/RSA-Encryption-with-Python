#print('p')
#p = input()
#print('q')
#q = input()

p,q=89,107
print(p,q)
n=p*q
fi=(p-1)*(q-1)
list_all=[]


def co_prime(number):
    list1=[]
    for i in range(number-1):
        if number%(i+1)==0: 
            list1.append(i+1)
    list1.append(number)
    list1.remove(1)
    return(list1)
    
def remove_co_prime(list):
    for i in list:
        for ii in range(1,n//2):
            if ii*i in list_all:
                list_all.remove(i*ii)
def remove_bigger(list):
    for i in list:
        if i in list_all:
            list_all.remove(i)
    
    
for i in range(2,n):
     list_all.append(i+1)

def dec_key(en):
    i = 2
    while i<20:
        formula=(1+fi*i)%en
        dec=int((1+fi*i)/en)
        if (formula==0 and dec!=en):
            return(dec)
        i=i+1

def encrypt(val):
    cypher=(val**en)%n
    return (cypher)

def decrypt(val):
    decr=(val**dec)%n
    return(decr)
        
        


  
list_n=co_prime(n)
list_fi=co_prime(fi)

#remove_co_prime(list_n) # moet weg als e wel een coprime van n mag zijn
remove_co_prime(list_fi)

listbigger=[]


        
for i in list_all:
    if i>fi:
        listbigger.append(i)
        
remove_bigger(listbigger)
en=3#list_all[0] 
print('encryption keys are: ', list_all)
dec=dec_key(en)
print('decryption keys is:',dec)
    
val=ord(input('text: '))
encrypte=encrypt(val)
print('encrypted test: ', encrypte)
decrypt=chr(decrypt(encrypte))
print('encrypted test: ', decrypt)





        
