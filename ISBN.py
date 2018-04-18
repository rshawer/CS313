#  File: ISBN.py

#  Description: code that checks for valid ISBNs

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/29/17

#  Date Last Modified: 10/30/17

# removes the X and replaces it with a 10, only used if it passes charactercheck
def removex(ISBNlist):
     for j in range(0,len(ISBNlist)):
        if(ISBNlist[j]=="X"):
            ISBNlist.remove("X")
            ISBNlist.append(10)
     return ISBNlist
    
#checks to make sure there are 10 numbers
def listlength(ISBNlist):
    return len(ISBNlist)==10

#checks to make sure the numbers are 0-9, and X only as the last digit
def charactercheck(ISBNlist):
   count=0
   for j in range(0,len(ISBNlist)):
       if(ISBNlist[j]=="0" or ISBNlist[j]=="1"  or ISBNlist[j]=="2" or ISBNlist[j]=="3" or ISBNlist[j]=="4" or ISBNlist[j]=="5" or ISBNlist[j]=="6" or ISBNlist[j]=="7" or ISBNlist[j]=="8" or ISBNlist[j]=="9" or (ISBNlist[j]=="X" and j==len(ISBNlist)-1)):
           count+=1
   return count==10
       
#partial sum checked to see if divisible by 11
def partialsum(ISBNlist):
    s1=[]
    s2=[]
    sum1=0
    sum2=0
    for i in ISBNlist:
        sum1+=int(i)
        s1.append(sum1)
    for i in s1:
        sum2+=int(i)
        s2.append(sum2)
    if(sum2%11==0):
        return True

def main ():
  # open file for reading
  in_file = open ("./isbn.txt", "r")
  # open file for writing
  out_file = open ("isbnOut.txt", "w")
  # read the number of ISBN strands
  num_lines=len(in_file.readlines())
  in_file.seek(0)
  # read the ISBN strands properly
  ISBNlist=[]
  for i in range(num_lines):
    string1 = in_file.readline()
    string1 = string1.strip()
    string2 = string1
    string1 = string1.replace('-',"")
    string1 = string1.upper()
  #determines if ISBN is valid or invalid                                                                                                                                                                                        
    for i in string1:
     ISBNlist.append(i)
  #Turn all X to 10, if the X is at the end
    if(listlength(ISBNlist) and charactercheck(ISBNlist)):
     removex(ISBNlist)
     if(partialsum(ISBNlist)):
  #writes the valid invalid lines
        out_file.write (string2+" valid\n")
     else:
        out_file.write (string2+" invalid\n")
    else:
       out_file.write (string2+" invalid\n")
    ISBNlist=[]
#closes the file
  in_file.close
  out_file.close
     

main()
  
      
