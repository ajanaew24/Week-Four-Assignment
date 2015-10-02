__author__ = 'alicia.williams'

# CIS-125 FA 2015
# Week 4: piggetty.py
# File: piggetty.py 
# Code to create the way to completely translate all words into the correct Pig
# Latin Terms


# Define a function called piggy(string) that returns a string

vowels = "aeiouAEIOU"
	
# Loop through word, one letter at a time
# Collaboration with Rebekah Orth throughout

def piggy(word):
	n = 0
	endword = ""
	for letter in word:
		# Check if letter is a vowel
		if letter in vowels:
			if n == 0:
				# True?  We are done
				pig = word + "yay"
				return pig
			else:
				pig = word[n:] + endword + "ay"
				return pig
				
		else:
			endword = endword + word[n]
			n = n + 1

# Open the file *getty.txt* for reading.  
# (info in Ch. 5)
infile = open("getty.txt", "r")

# Open a new file *piggy.txt* for writing.  
outfile = open("piggy.txt", "w")

# Read the getty.txt file into a string.
stringgetty = infile.read()

# Strip out bad characters (, - .).
stringgetty = stringgetty.replace(",","")
stringgetty = stringgetty.replace("-","")
stringgetty = stringgetty.replace(".","")

# Split the string into a list of words.  
listgetty = stringgetty.split()

# Create a new empty string.  
gettypig = ""

# Loop through the list of words, pigifying each one.  
for word in listgetty:
	
# Add the pigified word (and a space) to the new string.  
    if len(word) > 0:
    	gettypig = gettypig + str(piggy(word)) + " "
	#print(piggy(word))

# Write the new string to piggy.txt.  
print(gettypig, file = outfile)


# close the files.
infile.close()
outfile.close()