import hashlib
import re

def findAnswer():
	md5Hash = ""
	key = "bgvyzdsv"
	intKey = 0

	while (re.match(r'00000', md5Hash) == None):
		m = hashlib.md5()
		m.update(key+str(intKey))
		md5Hash = m.hexdigest()
		intKey += 1

	print md5Hash
	return intKey - 1

print findAnswer()

