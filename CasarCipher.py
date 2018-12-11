def encrypt(text,s): 
    result = "" 
   
    for i in range(len(text)): 
        char = text[i] 
  
       	"""uppercase""" 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        """lowercase""" 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 
  
"""actual encription""" 
text = "My programming class is the most interesting experience I've had in my entire life!"
s = 4
print "Text  : " + text 
print "Shift : " + str(s) 
print "Cipher: " + encrypt(text,s) 
