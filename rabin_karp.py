def generate_hash(text, pattern):
    ord_text = [ord(i) for i in text]                              # stores unicode value of each character in text 
    ord_pattern = [ord(j) for j in pattern]       
    #print(ord_pattern)                 # stores unicode value of each character in pattern
    len_text = len(text)                                           # stores length of the text 
    len_pattern = len(pattern)                                     # stores length of the pattern
    len_hash_array = len_text - len_pattern + 1  
    #print(len_hash_array)                  # stores the length of new array that will contain the hash values of text
    hash_text = [0]*(len_hash_array)                               # Initialize all the values in the array to 0.
    hash_pattern = sum(ord_pattern)                                                
    for i in range(0,len_hash_array):                              # step size of the loop will be the size of the pattern
        if i == 0:                                                 # Base condition
            hash_text[i] = sum(ord_text[:len_pattern])             # initial value of hash function
        else:
            hash_text[i] = ((hash_text[i-1] - ord_text[i-1]) + ord_text[i+len_pattern-1])   # calculating next hash value using previous value
    return [hash_text, hash_pattern]                               # return the hash values

def Rabin_Karp_Matcher(text,pattern):
    text=str(text)
    pattern=str(pattern)
    hash_text,hash_pattern = generate_hash(text,pattern)

    len_text=len(text)
    len_pattern=len(pattern)
    flag =False

    for i in range(len(hash_text)):
        if hash_text[i]==hash_pattern:
            count=0
            for j in range(len_pattern):
                if pattern[j]==text[i+j]:
                    count +=1
                else:
                    break
            if count ==len_pattern:
                flag= True
                print("Pattern occurs at index",i)
    if not flag:
        print("Pattern is not at all present in the text")


#generate_hash("hellophilip","hello")
Rabin_Karp_Matcher("101110000011010010101101","1011")
Rabin_Karp_Matcher("ABBACCADABBACCEDF","ACCE")