
#imports SHA-1 algorithm
import hashlib

##operation for finding the inverse.
# <<https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm> 
# provided some implementation on how to get started
def RedefinedExtendedEuclidean(a, b):
    #print(a,b)
    if (a == 0):
        return (b, 0, 1)
    else:
        gcd, yequal, xremianing = RedefinedExtendedEuclidean(b % a, a)
        #b//a is floor division
        return (gcd, xremianing - (b // a) * yequal, yequal)

def InverseMod(a, m):
    gcd, xremianing, yequal = RedefinedExtendedEuclidean(a, m)
    #print(gcd,xremianing,yequal)
    if (gcd != 1):
        raise Exception('not defined')
    else:
        return xremianing % m


class Receiver(object):

  def __init__(self):
    #Stores the variables sincen they are technically private
    self._p =  123456791
    self._q =  987654323
    self.E_num =  127
    self.__GeneratePhiN__()

  def __GenerateN__(self):
    self.n = self._p * self._q
    
  def __GeneratePhiN__(self):
    self.Phin = (self._p-1) * (self._q-1)

  def SendNandE__(self):
    self.__GenerateN__()
    return self.n,self.E_num
  
  def __FindD__(self):
    self.D = InverseMod(self.E_num, self.Phin)

  def Encrypt__(self,cipher):
    self.__FindD__()
    #print("The decryption D is: ", self.D)
    #Bob signs the each byte of the hex using his private key. m ^ self.D mod self.n 
    plaintext = [pow(int(cipher[i],16),self.D,self.n) for i in range(0, len(cipher))]

    #turn it into a hexadecimal string and then join them together 
    x =  ['{:x}'.format(i) for i in plaintext]
    #print("cipher is", x)
    plain = ''.join(x)
    print("The hex of the RSA signed hashed message is:" , plain)
    return x
  
   
  

class Sender(object):

  def Decrypt__(self,cipher,n,e):
    #print("decrypting cipher message", cipher)
    #Alice decrypts the hash DS using Bobs public key that was sent
    ciphertext = [pow(int(cipher[i],16),e,n) for i in range(0, len(cipher))]
    ciphertext = ['{0:x}'.format(i) for i in ciphertext]

    #This is a bit of string fixing that has to be done. '.format' does not return a leading zero, so if we joined the list,
    # we will be missing some zeros. This code fixes that issue
    output = []
    for i in ciphertext:
      #print(i)
      if (len(i) == 1):
        i = "0" + i
        #print(i)
        output.append(i)
      else:
        output.append(i)

    return ''.join(output)

  def verify__(self, hashed, message_str):
    result = hashlib.sha1(message_str.encode())
    hex_message = resu.hexdigest()
    print('')
    print("hashing public original message.....")
    print(hex_message)
    print("Decrypting digital signature hash...")
    print(hashed)
    print("message hash and decrypted hash are correct") if(hashed == hex_message) else print("not correct hash..message tampered")

  

if __name__ == "__main__":
  Alice = Sender()
  Bob = Receiver()
 

  #message that requires signing. This is Bob's message that requires he sign it
  messsage_str = "Good Morning and have a nice days"
  print(messsage_str)

  #we use SHA-1 since it limits the message hash to 160 bit. A requirement specificied in Assignment 7
  resu = hashlib.sha1(messsage_str.encode())
  x = resu.hexdigest()
  print("The output hash(SHA-1) for the message is: ", resu.hexdigest())
  
  #In RSA we need the m < n  before we do the m ^ key mod n. Since the hash message is larger than  'n' which we specified to be
  #123456791 * 987654323 = n, we have to split the hash message into blocks so that m < n is satisfied. For this project I use each bytes (2 characters each) 
  #in the hex message format and did the calculations on that byte. For example a hash message of 0xdd...... will have the int(dd) ^ key mod n, and then finish all the 
  #remaining bytes of the hex using the same method. 
  hash_to_byte = [ x[i:i+2] for i in range(0, len(x), 2)]
  #print(hash_to_byte)
 
  #Bobs sends n and e to Alice
  n,e = Bob.SendNandE__()

  #now Bob encrypt/signs the hash message using his private key.
  hash_message = Bob.Encrypt__(hash_to_byte)
 
  #Alice reads the message and the Digital signature. She decrypts the RSA signed DS with Bobs public key.
  print("\nDecrypting the signed hash now using public key and verifying if correct\n")
  digital_signature = Alice.Decrypt__(hash_message,n,e)

  #To check if the message has been sent correctly, Alice will check if the hash message she gets after decrypting is the same hash of the orginal message (the orginal message is sent to Alice too, she just needs to do a hash on it).
  # If the message is the same there was no tampering. 
  Alice.verify__(digital_signature, messsage_str)