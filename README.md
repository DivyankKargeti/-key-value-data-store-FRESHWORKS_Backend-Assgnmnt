# -key-value-data-store-FRESHWORKS_Backend-Assgnmnt

# How to Run the Code

### Steps:-

1. Open the CMD and move to the project directory
2. Open Command Prompt
3. In the CMD, Run the Python Idle terminal by using the following command: ``` >>>python ```
4. Now a Python repl will open up in the Command Prompt
5. Use the following Code for understanding the working:
```python

	#importing the main file
	import code as x 
	
	#to create a key with key_name,value given and with NO TTL(Time to Live) Argument
	x.create("Divyank",17)
	#to create a key with key_name,value given and with a TTL(Time to Live) Argument of 3600 secs
	x.create("Siddartha",45,3600) 
	
	#Reading data
	x.read("Divyank")
	x.read("Siddartha")
	
	#Deleting data
	x.delete("Divyank")
	x.delete("Siddartha")
	
	
	###Extras
	#we can access these using multiple threads like
        t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
        t1.start()
        t1.sleep()
        t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
        t2.start()
        t2.sleep()

	
```

## Screen Shots of the Working Code:

		

## Problem Statement

This is a file which can be exposed as a library that supports the basic CRD(create, read, write) operations. Data store is meant to local storage for one single process on single laptop

The data store will support the following :
1. It can be initialized using an optional file path. If one is not provided, it will reliably 
create itself in a reasonable location on the laptop.
2. A new key-value pair can be added to the data store using the Create operation. The key 
is always a string - capped at 32chars. The value is always a JSON object - capped at 
16KB.
3. If Create is invoked for an existing key, an appropriate error must be returned.
4. A Read operation on a key can be performed by providing the key, and receiving the 
value in response, as a JSON object.
5. A Delete operation can be performed by providing the key.
6. Every key supports setting a Time-To-Live property when it is created. This property is
optional. If provided, it will be evaluated as an integer defining the number of seconds 
the key must be retained in the data store. Once the Time-To-Live for a key has expired, 
the key will no longer be available for Read or Delete operations.
7. Appropriate error responses must always be returned to a client if it uses the data store in 
unexpected ways or breaches any limits
8. The file size never exceeds 1GB
9. The file is accessed by multi-threading


