# Danny has a possible list of passwords of Manny's facebook account. All passwords length is odd. But Danny knows that Manny is a big fan of palindromes. So, his password and reverse of his password both should be in the list.

# You have to print the length of Manny's password and it's middle character.

# Note : The solution will be unique.

# INPUT
# The first line of input contains the integer N, the number of possible passwords.
# Each of the following N lines contains a single word, its length being an odd number greater than 2 and lesser than . All characters are lowercase letters of the English alphabet.

# OUTPUT
# The first and only line of output must contain the length of the correct password and its central letter.

# CONSTRAINTS

# SAMPLE INPUT 
# 4
# abc
# def
# feg
# cba
# SAMPLE OUTPUT 
# 3 b

n=int(input())
lis=[]
for i in range(n):
    lis.append(input())
print(lis)
# for i in range(len(lis)):
#     for j in range()
