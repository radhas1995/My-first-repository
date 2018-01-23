import string
dict1 = dict()
def count_not_a_article():
	count  = 0
	file1 = open("Book-1.txt") # opening the book

	for line in file1:	
		a = line.split()
		for word in a:
			if word not in ["a", "the", "at", "run", "to","and","are","or","for","an","this"]:
				count = count + 1
	print ("total num of words not including articles",count)
count_not_a_article()
