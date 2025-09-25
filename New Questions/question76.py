"""Write a program that accepts a comma separated sequence of words as input and
 prints the words in a comma-separated sequence after sorting them alphabetically.
 Suppose the following input is supplied to the program:
 without,hello,bag,world
 Then, the output should be:
 bag,hello,without,world"""

input_sequence = input("Enter a comma-separated sequence of words: ")
words = input_sequence.split(',')
sorted_words = sorted(words)
sorted_sequence = ','.join(sorted_words)
print("Sorted words:", sorted_sequence)