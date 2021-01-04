"""This program demonstrates RSA naive way given a n,q,e,and m """


#recursive euclidean alogirthm 
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

##operation for finding the inverse.
# <<https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm> 
# provided some implementation on how to get started on recursive extended euclidean
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
    #Stores the variables since they are technically private
    self._p =  123456791
    self._q =  987654323
    self.E_num =  127
    self.__GeneratePhiN__()

  #generates the N = p*q
  def __GenerateN__(self):
    self.n = self._p * self._q
  
  #generates phi(n)
  def __GeneratePhiN__(self):
    self.Phin = (self._p-1) * (self._q-1)

  #sends the n and e to receiver
  def SendNandE__(self):
    self.__GenerateN__()
    return self.n,self.E_num
  
  #calculates the inverse of E mod n
  def __FindD__(self):
    self.D = InverseMod(self.E_num, self.Phin)

  #Decrpts the message
  def Decrypt__(self,cipher):
    self.__FindD__()
    print("The decryption D is: ", self.D)
    plaintext = pow(cipher, self.D, self.n)
    return plaintext




class Sender(object):
  #encrypts senders message using n and e.
  def Encrypt__(self,message,n,e):
    if(message < n):
      ciphertext = pow(message,e,n)
    else:
      raise Exception('Error')
    return ciphertext








if __name__ == "__main__":

  #initialize
  Alice = Sender()
  Bob = Receiver()

  #Bob should be randomly generating p and q but in this case, we already know p and q
  message = 14152019010605
  print("Orginal message: ", message)

  #bobs sends Alice N and E. 
  n,e = Bob.SendNandE__()

  #Alice encrypts the mesage and sends it to b
  ciphertext = Alice.Encrypt__(message,n,e)
  print("Ciphertext is: ", ciphertext)

  #Bob decrypts the message
  print("\nDecrypting the ciphertext now....\n")
  plaintext = Bob.Decrypt__(ciphertext)
  print("Plaintext result after decryption: ", plaintext)







  
    






  
