letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]
print(backwards)                #With a negative step, the start value defaults to the end of the string, and the stop value defaults to the beginning of the stream
 #"Reversing the sequence"

#slice to produce qpo
backwards = letters[16:13:-1]
print(backwards)
#slice to produce edcba
backwards = letters[4::-1]
print(backwards)
#slice to produce zyxwvuts
backwards = letters[:17:-1]     #or you can use print(letters[:-9:-1])
print(backwards)

print(letters[-1:])             #returns the end of the sequence 
print(letters[:1])              #returns the first character of the sequence
print(letters[0])               #same as first character of sequence but has some weird issues


