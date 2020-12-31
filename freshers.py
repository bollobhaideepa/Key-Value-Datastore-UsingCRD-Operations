# importing threading to perform thread operations
import threading 
from threading import*
import time

dictionary={} #'dictionary' id the dictionary which store the data in key-value pairs
timeout=3600

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in dictionary:
        print("error: this key already exists") #error message
    else:
        if(key.isalpha()):
            if len(dictionary)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    store=[value,timeout]
                else:
                    store=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dictionary[key]=store
            else:
                print("error: Memory limit exceeded!! ")#error message
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key") #error message
    else:
        b=dictionary[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to retur the value in the format of JasonObject i.e.,"key:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key") #error message
    else:
        b=dictionary[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del dictionary[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message
        else:
            del dictionary[key]
            print("key is successfully deleted")

#We ca also perform modify operation to change the value of key before its expiry time if provided

def modify(key,value):
    b=dictionary[key]
    if key not in dictionary:
        print("Enter existing key to modify:")
    elif b[1]!=0:
        if time.time()<b[1]:
            if key not in dictionary:
                print("error: given key does not exist in database. Please enter a valid key") #error message
            else:
                store=[]
                store.append(value)
                store.append(b[1])
                dictionary[key]=store
        else:
            print("error: time-to-live of",key,"has expired") #error message
    else:
        if key not in dictionary:
            print("error: given key does not exist in database. Please enter a valid key") #error message
        else:
            store=[]
            store.append(value)
            store.append(b[1])
            dictionary[key]=store


while(1):
    user_choice=int(input("CRD operations of Your Choice:\n 1.create \n 2.read \n 3.delete\n 4.modify \n 0.Exit \n Enter any of 3 number to perform operations:\n"))
        

    if user_choice==1:
        key_input=input("Enter Key:")
        value_input=int(input("Enter Value:"))
        create(key_input,value_input)
        print("key,value pairs in dictionary:",dictionary)    
    elif user_choice==2:
        key_input=input("Enter Key:")
        re=read(key_input)
        print(re)
        print("key,value pairs in dictionary:",dictionary)
    elif user_choice==3:
        key_input=input("Enter Key:")
        delete(key_input)
        print("key,value pairs in dictionary:",dictionary)
    elif user_choice==4:
        key_input=input("Enter Key:")
        value_input=input("Enter Value:")
        modify(key_input,value_input)
        print("key,value pairs in dictionary:",dictionary)
    elif user_choice==0:
        break
    else:
        print("Please Enter any of CRD opeartions")
    print()
#we can access these using multiple threads like
thread1=Thread(target=(create or read or delete),args=(key_input,value_input,timeout)) #as per the operation
thread1.start()
thread2=Thread(target=(create or read or delete),args=(key_input,value_input,timeout)) #as per the operation
thread2.start()
thread3=Thread(target=(create or read or delete),args=(key_input,value_input,timeout)) #as per the operation
thread3.start()
#and so on upto N number of Thread





