#module(s)
import os
import json
import time
import threading

lock = threading.Lock()
#Specify your directory here
path = "PieDB/keys"

#initialization of directory
try:
	os.makedirs(path)
except FileExistsError:
	pass

#exceptions

#main base exception
class DatabaseError(Exception):
	def __init__(self, msg="An error has occurred with the database."):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for an empty database
class EmptyDatabaseError(DatabaseError):
	def __init__(self, msg="There has been no keys created in the database, yet."):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for not providing a string for a key
class KeyNameError(DatabaseError):
	def __init__(self, msg="The key for the object must be a string"):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for when a key does not exists
class KeyNotFoundError(DatabaseError):
	def __init__(self, msg="That key does not exists."):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for when a key already exists (for the create command)
class KeyExistsError(DatabaseError):
	def __init__(self, msg="That key already exists."):
		self.msg=msg
		super().__init__(self.msg)
		
#input exceptions

# exception for no input & base exception for input exceptions
class NoInputError(DatabaseError):
	def __init__(self, msg="You must specify a key and/or value to create"):
		self.msg=msg
		super().__init__(self.msg)
		
# exception when no key for an object has been provided
class NoKeyError(NoInputError):
	def __init__(self, msg="You must specify a key"):
		self.msg=msg
		super().__init__(self.msg)
# exception for when no value for an object has been provided
class NoValueError(NoInputError):
	def __init__(self, msg="You must specify a value"):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for no input to set
class NoInputToSet(NoInputError):
	def __init__(self, msg="You must specify a key and/or value to set"):
		self.msg=msg
		super().__init__(self.msg)
		
# exception for no input to update
class NoInputToUpdate(NoInputError):
	def __init__(self, msg="You must specify a key and/or value to update"):
		self.msg=msg
		super().__init__(self.msg)

# exception for High Length of Key		
class HighLengthKey(DatabaseError):
    	def __init__(self, msg="The Key Should Be of 32 Characters"):
    			super().__init__(msg=msg)

# exception for High Length of Value
class HighLengthValue(DatabaseError):
    	def __init__(self, msg="The value must be of 16 KiloBytes"):
    			super().__init__(msg=msg)
#functions

#timetolive
def ttl(key):
    os.remove("{}/{}.json".format(path,key))


#create key function
def create(key, value, timetolive=""):
	with lock:
		if key is None:
				raise NoKeyError
		else:
			pass
		if value is None:
			raise NoValueError
		else:
			pass
		if type(value) is dict:
				pass
		else:
				print("The Value must be JSON Object.")
		if len(key) > 32:
				raise HighLengthKey
		else:
				pass
		if len(value) > 16000:
				raise HighLengthValue
		else:
				pass
		try:
			if isinstance(key, str):
				try:
					try:
						with open("{}/{}.json".format(path,key), "x") as file:
							try:
								json.dump(value,file)
							finally:
								file.close()
							print('Key "{}" with value "{}" has been created'.format(key, value))
					except FileNotFoundError:
						if FileNotFoundError:
							try:
								os.makedirs("{}/".format(path))
							except FileExistsError:
								pass
							with open("{}/{}.json".format(path,key), "x") as file:
								try:
									json.dump(value,file)
								finally:
									file.close()
								print('Key "{}" with value "{}" has been created'.format(key, value))
				except FileExistsError:
					if FileExistsError:
						raise KeyExistsError('The key named "{}" has already been found in the database'.format(key))
			else:
				raise KeyNameError
		except TypeError:
			if TypeError:
				raise NoInputError
		if timetolive is None:
				return
		else:
				try:
					time.sleep(timetolive)
					ttl(key)
				except:
					pass		

#read key function
def read(key):
    with lock:
					if isinstance(key, str):
							try:
								with open("{}/{}.json".format(path,key), "r") as file:
									try:
										y = json.load(file)
										return y
									finally:
										file.close()
							except FileNotFoundError:
								raise KeyNotFoundError('No such key named "{}" has been found in the database'.format(key))
					else:
						raise KeyNameError


#update value function
def update(key, new_value):
	if key is None:
		raise NoKeyError
	else:
		pass
	if new_value is None:
		raise NoValueError
	else:
		pass
	try:
		if isinstance(key, str):
			try:
				try:
					try:
						open("{}/{}.json".format(path,key), "x")
					except FileExistsError:
						if FileExistsError:
							with open("{}/{}.json".format(path,key), "w") as file:
								try:
									json.dump(new_value,file)
								finally:
									file.close()
								print('Key "{}" has had its value changed to "{}".'.format(key, new_value))
				except FileNotFoundError:
					if FileNotFoundError:
						try:
							os.makedirs("{}/".format(path))
						except FileExistsError:
							pass
						try:
							open("{}/{}.json".format(path,key), "x")
						except FileExistsError:
							if FileExistsError:
								with open("{}/{}.json".format(path,key), "w") as file:
									try:
										json.dump(new_value,file)	
									finally:
										file.close()
									print('Key "{}" has had its value changed to "{}".'.format(key, new_value))
			except FileExistsError:
				if FileExistsError:
					try:
						open("{}/{}.json".format(path,key), "x")
					except FileExistsError:
						if FileExistsError:
							with open("{}/{}.json".format(path,key), "w") as file:
								try:
									json.dump(new_value,file)	
								finally:
									file.close()
								print('Key "{}" has had its value changed to "{}".'.format(key, new_value))
		else:
			raise KeyNameError
	except TypeError:
		if TypeError:
			raise NoInputError
		
		
#delete key function
def delete(key):
	with lock:
		if isinstance(key,str):
			try:
				os.remove("{}/{}.json".format(path,key))
				print(key, "has been deleted from the database.")
			except FileNotFoundError:
				if FileNotFoundError:
					raise KeyNotFoundError('No such key named "{}" has been found in the database'.format(key))
		else:
			raise KeyNameError	
