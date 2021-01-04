#simpleaes.py

Simple AES is a 128-bit ECB (Electric Code Book) encryption algorithm. 

## special information
-I set the key and the plaintext box already as an ASCII value that I can readily translate to hex.
 This was done for convenience of the coding where I needed to check for errors and how the elements move around.
 
-For how the list of list is created, it is done column wise. So lets say for the figure below:
               B_1    B_5    B_9    B_13
               B_2    B_6    B_10   B_14
               B_3    B_7    B_11   B_15
               B_4    B_8    B_12   B_16

                  column 1                  column 2
               [[B_1, B_2, B_3, B_4] , [B_5, B_6, B_7, B_8], ...]
-So when we do the mix column operation we have to delist the data to a temporary row then do the operations of shifting. 

-I have done as much unit testing as I can to the function and their inverse. If we input a file to regular function and use that output for the
 input of the inverse, we should get the orginal input back. I have also used the identity matrix to check.


##Usage
-This program runs on Python 3. 
-Run the main.py (python3 main.py)

##Author
-Justine Gausin
