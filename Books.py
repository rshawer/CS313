#  File: Books.py

#  Description: Compares the vocabulary of two books and their authors

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 12/3/17

#  Date Last Modified: 12/3/17

# Create word dictionary from the comprehensive word list 

word_dict = {}
def create_word_dict ():
    dictionary = open("./words.txt","r")
    for line in dictionary:
        line=line.strip()
        word_dict[line]=1
    dictionary.close()
# Removes punctuation marks from a string
def parseString (st):
  s=""
  for i in range (len(st)):
    if (st[i].isalpha()):
      s+=st[i]
    elif (st[i].isspace()):
      s+=st[i]     
    elif (st[i]=="'") and (i!=len(st)-1) and (st[i+1]!='s') and (st[i+1]!=" "):
      s+=st[i]
    else:
      s+=" "
  return s
# Returns a dictionary of words and their frequencies
def getWordFreq (file):
    book = open(file,"r", encoding = 'utf8')
    new_dict={}
    for line in book:
        line=line.strip()
        line=parseString(line)
        wordlist=line.split()
        for word in wordlist:
            if word in new_dict:
                new_dict[word]=new_dict[word]+1
            else:
                new_dict[word]=1
    capitallist=[]
    for word in new_dict:
        if word[0].isupper() and word not in capitallist:
            capitallist.append(word)
    for word in capitallist:
        check=word.lower()
        if check in new_dict:
            new_dict[check]=new_dict[check]+new_dict[word]
        elif check in word_dict:
            new_dict[check]=new_dict[word]

    for word in capitallist:
        del new_dict[word]
    book.close()
    return new_dict
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
    D=set()
    H=set()
    for key in freq1:
        D.add(key)
    for key in freq2:
        H.add(key)
    total1=0
    total2=0
    dminush=D-H
    hminusd=H-D
    for word in dminush:
        total1+=freq1[word]
    for word in hminusd:
        total2+=freq2[word]
    print(author1)
    print("Total distinct words =",len(freq1))
    print("Total words (including duplicates) =",sum(freq1.values()))
    print("Ratio (% of total distinct words to total words) =",len(freq1)/(sum(freq1.values()))*100)
    print()
    print(author2)
    print("Total distinct words =",len(freq2))
    print("Total words (including duplicates) =",sum(freq2.values()))
    print("Ratio (% of total distinct words to total words) =",len(freq2)/(sum(freq2.values()))*100)
    print()
    print(author1,"used",len(dminush),"words that", author2, "did not use.")
    print("Relative frequency of words used by", author1, "not in common with",author2,"=", total1/sum(freq1.values())*100)
    print(author2,"used",len(hminusd),"words that", author1, "did not use.")
    print("Relative frequency of words used by", author2, "not in common with",author1,"=", total2/sum(freq2.values())*100)          
def main(): 
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
