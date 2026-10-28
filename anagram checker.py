word1=input('enter a word :')
word2=input('enter a word :')
word_list1=sorted(list(word1.replace(" ","").lower()))
word_list2=sorted(list(word2.replace(" ","").lower()))
print(word_list1)
print(word_list2)
if word_list1 == word_list2:
    print('condition 1 satisfied')
    if len(word_list1)==len(word_list2):
     print('conditon 2 is satisfied')
     print('the words are anagrams of each other')
    else:
       print('words are not anagrams')
else:
   print('words are not anagrams')  