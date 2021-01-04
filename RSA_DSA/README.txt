#RSA_DSA_naive.py

The program is a simple configuration simulating RSA style digital signature. 

##Usage 
Python 3.x is the normal enviroment for the program

#Special Notes. 
    - I used the same variables (p,q,e) from the previous assignment of just RSA.
    - In RSA we need the m < n  before we do the m ^ privkey mod n. Since the hash message ('m' , 160 bits long) is larger than 'n' which we specified to be
      123456791 * 987654323 = n, we have to split the hash message into blocks so that m < n is satisfied. For this project I use each bytes (2 characters each) 
      in the hex message format and did the calculations on that byte. For example a hash message of 0xdd....... will have the int(dd) ^ key mod n, and then finish all the 
      remaining bytes of the hex using the same method. Since m < n (n is not even 160 bits for this example), then the signed message will be as large as the original message!!!!
      IF we did choose 'n' that is slightly larger than 'm', then we did not have to do this method. 

#Author 
/Justine Gausin