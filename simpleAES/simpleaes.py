Sbox =(     0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
            0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
            0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
            0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
            0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
            0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
            0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
            0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
            0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
            0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
            0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
            0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
            0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
            0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
            0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
            0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
            0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
            0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
            0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
            0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
            0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
            0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
            0x54, 0xbb, 0x16)   
Inv_Sbox= (0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
            0x9e, 0x81, 0xf3, 0xd7, 0xfb , 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f,
            0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb , 0x54,
            0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b,
            0x42, 0xfa, 0xc3, 0x4e , 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24,
            0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25 , 0x72, 0xf8,
            0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,
            0x65, 0xb6, 0x92 , 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
            0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84 , 0x90, 0xd8, 0xab,
            0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3,
            0x45, 0x06 , 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1,
            0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b , 0x3a, 0x91, 0x11, 0x41,
            0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6,
            0x73 , 0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9,
            0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e , 0x47, 0xf1, 0x1a, 0x71, 0x1d,
            0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b ,
            0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
            0xfe, 0x78, 0xcd, 0x5a, 0xf4 , 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
            0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f , 0x60,
            0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f,
            0x93, 0xc9, 0x9c, 0xef , 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5,
            0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61 , 0x17, 0x2b,
            0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55,
            0x21, 0x0c, 0x7d)


Rcon = (0x00, 0x01, 0x02, 0x04, 
          0x08, 0x10, 0x20, 0x40, 
          0x80, 0x1b, 0x36)

def list_to_hex(s):
  temp = ""
  for x in range(4):
    for y in range(4):
      temp +='{:x}'.format(int(s[x][y]))
  return temp
  

class AES(object):
  def __init__(self):
    print("")


  #we turn the key into a list of list organized by columns 
  def get_key(self):
    orignial_key = []
    newrow= []
    for l in range(len(self.key)):
      orignial_key.append(ord(self.key[l]))
        #print (orignial_key)
    for r in range(4):
      newrow.append(orignial_key[r:r+4])
    self.key = newrow
    return newrow

  #we turn the plaintxt into a matrix of 4x4
  def plain_to_matrix(self):
    "create a list of a 4x4 matrix using an array"
    s1= [list(self.plain[i:i+4]) for i in range( 0, len(self.plain),4)]
    s2 = []
    for x in range(4):
      for y in range(4):
        s2.append(ord(s1[x][y]))
    #print("S2 is" ,s2)
    return [list(s2[i:i+4]) for i in range( 0, len(s2),4)]


  """             KEY OPERATION
                  W(1)   W(2)   W(3)   W(4)   --->

                B_1    B_5    B_9    B_13
                B_2    B_6    B_10   B_14
                B_3    B_7    B_11   B_15
                B_4    B_8    B_12   B_16

                    column 1                  column 2
                [[B_1, B_2, B_3, B_4] , [B_5, B_6, B_7, B_8] ...]
  """

  #Rcon for a 128 bit will only go up to 0x36 for 10 rounds. I added a pad of 0x00 to the begining so we can call the placement more easily. Example, at round 1 Rcon[1] is at 0x01
  #this is for the ley scedule. [a b c d]  is rotated to be [b c d a]

  def transformation(self, key1, roundnumber):
    tempkey= key1[1:] + key1[:1]
    for i in range(4):
      tempkey[i] = Sbox[tempkey[i]]
    tempkey[0] ^= Rcon[roundnumber]

    #print("Roundnumber is ", roundnumber)
    #print( "Rcon is ", Rcon[roundnumber])
    return tempkey

  #we expand the keys into 44 columns.  Using the key transformation and/or XOR, we would arrive at each keys 
  def expansion_keys(self):
    master_key = self.key
    for i in range(4,44):
      #print(i)
      key = []
      tempkey = []
      if(i % 4 == 0):
        tempkey = self.transformation(master_key[i-1], int(i/4))
        for l in range(4):
          #print(l)
          key.append(master_key[i-4][l] ^ tempkey[l])
        master_key.append(key)
      else:
        for l in range(4):
          key.append(master_key[i-4][l] ^  master_key[i-1][l])
        master_key.append(key)
      #print(key)
      #print("")
    return master_key

  #get key from expansion for the needed round.
  def get_key_expansion(self, master_key, roundnumber):
    return master_key[roundnumber*4:(roundnumber*4+4)]
    
  #we add the round key. Essentially its a key XOR column of state
  def add_roundkey(self, key, column):
    "This returns a list of list"
    l = []
    for x in range(4):
      for y in range(4):
        xor_val = key[x][y] ^ (column[x][y])
        l.append(xor_val)
    #return l
    #returns a list of list for sub byte
    return [ list(l[i:i+4]) for i in range(0,16,4)]
  

  #we subtitute the bytes using the Sbox    
  def sub_bytes(self, s):
    for i in range(4):
      for j in range(4):
        s[i][j] = Sbox[s[i][j]]
    return s 
  
  #we subtitute the bytes using the Inverse Sbox    
  def Inv_sub_bytes(self,s):
    for i in range(4):
      for j in range(4):
        s[i][j] = Inv_Sbox[s[i][j]]
    return s
  
    
  def shift_row_left(self,s):
      """delist the list-of-list"""
      temprow = []
      for x in range(4):
        for y in range(4):
          temprow.append(s[x][y])
      #print("temp row is", temprow)
      newrow = []
      #print(temprow)
      #change it row wise then shift 
      for r in range(4):
        newrow.append(temprow[r::4])
        newrow[r] = newrow[r][r:] + newrow[r][:r]
      l= [ r[c] for c in range(4) for r in newrow]
      #print("l is",l )
      brp = [list(l[i:i+4]) for i in range( 0, 16,4)]
      #print("print", brp)
      return brp
  

  def shift_row_right(self, s):
    """delist the list-of-list"""
    temprow= []
    for x in range(4):
      for y in range(4):
        temprow.append(s[x][y])
    #print("shift row maybe is", temprow)
    newrow = []
    #print("temprow is", temprow)

    for r in range(4):
      newrow.append( temprow[r::4] )
      newrow[r] = newrow[r][4-r:] + newrow[r][:4-r]
    brp = [ r[c] for c in range(4) for r in newrow ]
    #print("is this correct", brp)
    jack = [list(brp[i:i+4]) for i in range( 0, 16,4)]
    #print("this is jack", jack)
    return jack
    #return [ r[c] for c in range(4) for r in newrow ]


#implementation of the GF(2^8) <<https://en.wikipedia.org/wiki/Rijndael_MixColumns>> under C# example
  def FiniteFieldsGmul(self, a, b):
          p = 0
          for c in range(8):
              if b & 1:
                  p ^= a
              a <<= 1
              if a & 0x100:
                  a ^= 0x11b
              b >>= 1
          return p

  def Inv_mix_columns(self, s):
        """
                0E    0B    0D    09  
                09    0E    0B    0D
                0D    09    0E    0B 
                0B    0D    09    0E
        """
        #print("")
        #print(s)

        temprow= []
        for x in range(4):
         for y in range(4):
           temprow.append(s[x][y])
        #print(temprow)
        #print("")
        ss = []
        for c in range(4):
          col = temprow[c*4:(c+1)*4]
          #print(col)
          ss.append([
            self.FiniteFieldsGmul(0x0e, col[0]) ^self.FiniteFieldsGmul(0x0b, col[1]) ^self.FiniteFieldsGmul(0x0d, col[2]) ^self.FiniteFieldsGmul(0x09, col[3]),
            self.FiniteFieldsGmul(0x09, col[0]) ^self.FiniteFieldsGmul(0x0e, col[1]) ^self.FiniteFieldsGmul(0x0b, col[2]) ^self.FiniteFieldsGmul(0x0d, col[3]),
            self.FiniteFieldsGmul(0x0d, col[0]) ^self.FiniteFieldsGmul(0x09, col[1]) ^self.FiniteFieldsGmul(0x0e, col[2]) ^self.FiniteFieldsGmul(0x0b, col[3]),
            self.FiniteFieldsGmul(0x0b, col[0]) ^self.FiniteFieldsGmul(0x0d, col[1]) ^self.FiniteFieldsGmul(0x09, col[2]) ^self.FiniteFieldsGmul(0x0e, col[3])
          ])
        return ss
  def mix_columns(self, s):
    ss = [] 
    """      2 3 1 1          1 = value remains the same 
             1 2 3 1 
             1 1 2 3
             3 1 1 2 """
    #print(s)
    temprow = [] 
    for x in range(4):
      for y in range(4):
        temprow.append(s[x][y])

    for c in range(4):
            col = temprow[c*4:(c+1)*4]
            #print(col)
            #we can append([ ] ) or use extend (())
            ss.append([
                        self.FiniteFieldsGmul(0x02, col[0]) ^ self.FiniteFieldsGmul(0x03, col[1]) ^ col[2] ^ col[3] ,
                        col[0]  ^ self.FiniteFieldsGmul(0x02,col[1]) ^ self.FiniteFieldsGmul(0x03,col[2]) ^ col[3] ,
                        col[0]  ^ col[1]  ^ self.FiniteFieldsGmul(0x02,col[2]) ^ self.FiniteFieldsGmul(0x03,col[3]),
                        self.FiniteFieldsGmul(0x03,col[0]) ^ col[1]  ^ col[2]  ^ self.FiniteFieldsGmul(0x02, col[3]),
            ])
    return ss

  def encrypt(self, key, plain):
    self.key = key
    self.plain = plain
    k = self.plain_to_matrix()
    print("plaintext in hex form: ", list_to_hex(k))
    self.get_key()
    master = self.expansion_keys()
    #print(master)
    #print("")
    key0 = self.get_key_expansion(master, 0)
    state = self.add_roundkey(k, key0)
    #print("STaTE is ", state)
    for r in range(1, 10): 
      #print(r)   
      sub = self.sub_bytes(state)
      #print(sub)
      #print("")
      shift = self.shift_row_left(sub)
      #print(shift)
      k = self.mix_columns(shift)
      #print( k)      
      keyi = self.get_key_expansion(master, r)
      #print(keyi)
      state = self.add_roundkey(k, keyi)
    
    sub = self.sub_bytes(state)
    shift = self.shift_row_left(sub)
    

    keyi = self.get_key_expansion(master, 10)
    state = self.add_roundkey(shift, keyi)
    #print("")
    #print(state)
    return state

  def decrypt(self, key, plain):
    self.key = key
    self.plain = plain
    k = plain
    #k = self.plain_to_matrix()
    #print(k)
    self.get_key()
    master = self.expansion_keys()
    #print(master)
    #print("")
    key10 = self.get_key_expansion(master, 10)
    #print("key is for 10th round", key0)
    state = self.add_roundkey(k, key10)
    #print("state is ", state)
  
    for r in range(9, 0, -1):
      #print(r)
      #print("before the shift", state)
      shift = self.shift_row_right(state)
      #print("shift is:" , shift)
      sub = self.Inv_sub_bytes(shift)
      keyi = self.get_key_expansion(master, r)
      #print("key" ,keyi)
      k = self.add_roundkey(sub, keyi)
      state = self.Inv_mix_columns(k)
            

    shift  = self.shift_row_right(state)
    sub =  self.Inv_sub_bytes(shift)
    key0 = self.get_key_expansion(master, 0)
   # print("key0", keyi)
    state = self.add_roundkey(sub, key0)
    return state


   

#same as main.py. Just in case user runs simplaes.py instead of main. 

if __name__ == "__main__":
    #the key should be hexadecimal but here i just did ascii -> hexadecimal format. 
    key1 = "1a2b3c4d5e6f7g8h" #in hexadecimal 0x6162636465666768696a6b6c6d6f70710
    plaintext = "abcdefghijklmopq"  

    cipher = AES()
    encrypted_text = cipher.encrypt(key1, plaintext)
    print("Encrypting now..........Done\n")
    print("encrypted text is: ", list_to_hex(encrypted_text) )

    print('\ndecrpypting AES now.....')
    decrypted= AES()
    decry_text = decrypted.decrypt(key1, encrypted_text)
    print("decrypted text is: ", list_to_hex(decry_text))
    print("Does decrypted hex match plaintext in hex form?\n")
