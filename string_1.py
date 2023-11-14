word=input("Enter a word : ")
print("Given word is : ",word)
print("Word after inter change its 1st and last letter ")
swapped_wrd=word[-1]+word[1:-1]+word[0]
print(swapped_wrd)