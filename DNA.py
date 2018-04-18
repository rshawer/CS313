#  File: DNA.py

#  Description: This files find the common substrands between pairs of DNA strands

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/24/17

#  Date Last Modified: 10/25/17

 #returns true if there is no duplicates between two lists

def duplicatechecker(a,b):

    for i in range (len(a)):
        for j in range (len(b)):
            if(a[i]==b[j]):
                return False
            else:
                return True 

def main ():
  # open file for reading
  in_file = open ("./dna.txt", "r")

  # prints the header
  print("Longest Common Sequences")
  print()
  
  # read the number of pairs
  num_pairs = in_file.readline ()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)

  # read each pair of dna strands
  for i in range (num_pairs):
    st1 = in_file.readline()
    st2 = in_file.readline()

    st1 = st1.strip()
    st2 = st2.strip()

    st1 = st1.upper ()
    st2 = st2.upper ()
    print("Pair " + str(i+1)+": ", end="")
    # order the strands by size
    if (len(st1) > len (st2)):
      dna1 = st1
      dna2 = st2
    else:
      dna1 = st2
      dna2 = st1

    # get all substrands of dna2
    length=0
    match=[]
    wnd = len (dna2)
    counter=0
    duplicatestorage=[]
    while (wnd > 1):
      start_idx = 0
      while ((start_idx + wnd) <= len(dna2)):
        sub_strand = dna2[start_idx: start_idx + wnd]
        if(sub_strand in dna1):
            if(len(sub_strand)>=length):
             length=len(sub_strand)
             match.append(sub_strand)
      # move the window by one
        start_idx += 1
      # decrease the window size
      wnd = wnd - 1
    if len(match)==0:
       print("No Common Sequence Found")
    else:
       for i in range(len(match)):
        duplicatestorage.append(match[i])
        if(counter!=0 and duplicatechecker(duplicatestorage,match)):
         print("        "+match[i])
         duplicatestorage=[]
        if(counter==0):
         print(match[i])
         duplicatestorage=[]
        counter=+1
    print()
        
  # close the file
  in_file.close()

main()
