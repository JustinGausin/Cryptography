""" SIMPLIFIED 12 bit DES encryption 
            by: Justin Gausin
"""




#return 8 bit string 
def expansion(Ri):
  trueExpansion = Ri[0] + Ri[1] + Ri[3] + Ri[2] + Ri[3] + Ri[2] + Ri[4] + Ri[5]
  return trueExpansion


#returns an 8 bit string  
def XORfunction(L, R):
  Left = int(L,2)
  Right = int(R,2)
  resultz = (Left ^ Right)         #XOR 2 integers
  resultzString = '{0:08b}'.format(resultz)
  return resultzString

#returns a 6 bit string 
def XORfunction_LiSBox(Li, Sbox):
  Left1 = int(Li,2)
  Right1 = int(Sbox,2)
  resultingXOR = (Left1 ^ Right1)   #XOR 2 integers
  resultingXORstring = '{0:06b}'.format(resultingXOR)
  return resultingXORstring

#returns a string of Keyi (8 bits)
def Keyi(key,i):
  if (i == 0):
    Key_i = key[:-1]
  else:
    Key_i = key[i:] + key[:(i-1)]
  return Key_i



#If we want a dynamic key and input
##inputMain = raw_input("Enter the 12 bit input:  ")
##key = raw_input("Enter a 9 bit key:  ")



#Static Key and Input
inputMain = '001000001011'      # string binary 
print("Plaintext: ", inputMain)
#key number input
key = '110011011'               # 9 bit key value 
Length_sting = len(inputMain)   
first_length = round(Length_sting / 2)

##We split the string in half, creating our L0 and R0
## L0 and R0 are 6 bit strings 
L0input = inputMain[:first_length].lower()
R0input = inputMain[first_length:].upper()
#print(L0input)
#print(R0input)
#print('')

Li= L0input
Ri= R0input
SBox1Key = [ ['101', '010' , '001', '110', '011', '100', '111', '000'], ['001', '100', '110', '010', '000', '111', '101', '011']]

SBox2Key = [ ['100', '000', '110', '101', '111', '001', '011', '010'], ['101', '011', '000', '111', '110', '010', '001', '100']]

print("Original Key is: ", key)
print("")
for i in range(0,4):
  print("This is iteration number ", i+1)
  print("what is Li: ", Li)
  print("What is Ri: ", Ri)
  #Ri becomes the new Li
  Li_plus_One = Ri

  #subsa becomes an expanded 8 bit string of Rinput
  R_expanded = expansion(Ri)

  #get the key
  x =i
  Key_i = Keyi(key, x)
  print("What is the key:      ", Key_i)
  print("What is the exp:      ", R_expanded)
  #XOR key and R expanded
  XORKey_Rinput = XORfunction(R_expanded,Key_i)
  
  print("XOR key and R expanded", XORKey_Rinput)

  #separate into 2 binaries (4 bits each)
  lenXORE_Ki = len(XORKey_Rinput)
  len_gth = round(lenXORE_Ki/2)
  SBox1Input = XORKey_Rinput[:len_gth].lower()
  SBox2Input = XORKey_Rinput[len_gth:].upper()

  #value is a string changed into a integer
  print("Sbox1Input ", SBox1Input)
  print("Sbox2Input ", SBox2Input)
  column1 =int(SBox1Input[0])
  column2 =int(SBox2Input[0]) 

  #The last 3 bits determine the column 
  row1String = SBox1Input[1]+ SBox1Input[2]+ SBox1Input[3]
  row2String = SBox2Input[1]+ SBox2Input[2]+ SBox2Input[3]
  row1Int = int(row1String,2)
  row2Int = int(row2String,2)

  #find the Box ouputs... results is a string. 
  #Each output is 3 bits. the total of both is 6 bits
  SBox1ouput = SBox1Key[column1][row1Int]
  SBox2ouput = SBox2Key[column2][row2Int]
  SBoxResult = SBox1ouput + SBox2ouput
  print("Sbox output of both: ", SBoxResult )

  #XOR L0 to the Rinput. ouputs a 6 bit 
  XORofLi_SBox = XORfunction_LiSBox(Li, SBoxResult)
  Ri_plus_one = XORofLi_SBox
  print("The XOR of Li and SboxOut is", XORofLi_SBox)

  #create the new Li and Ri 
  Ri = Ri_plus_one
  Li = Li_plus_One

  print('')

Ciphertext = Li+Ri

print("Plaintext bits was : ", inputMain)
print("Final Ciphertext is: ",Ciphertext)
