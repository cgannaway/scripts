#reverse cipher

message = raw_input("Enter a string... ")

print message[::-1]

'''
base loop:

message = 'aksdjhfas;ldkjf'

encrypted = ''

i = len(message) -1

while i>=0:
    encrypted = encrypted + mess[i]
    i = i - 1

print encrypted
