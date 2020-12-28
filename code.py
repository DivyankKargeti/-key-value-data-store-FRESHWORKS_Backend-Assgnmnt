import threading 
from threading import*
import time

d={} #It is the dictionary in which we will be storing data

#for create operation 
#Usage: "create(key_name,value,timeout_value)" timeout is optional - We can also pass just 2 args

def create(key,value,timeout=0):
    if key in d:
        print("ERROR: This key is already present in datastore") #ERROR Msg1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("ERROR: Memory limit has exceeded ")#ERROR Msg2
        else:
            print("ERROR: Invalind type key - key_name must contain only alphabets and no special characters or numbers")#ERROR Msg3

#for read operation
#Usage: "read(key_name)"
            
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #ERROR Msg4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #ERROR Msg5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#Usage: "delete(key_name)"

def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #ERROR Msg4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #ERROR Msg5
        else:
            del d[key]
            print("key is successfully deleted")