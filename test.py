string = input() # abba, testtest
character = input() # c, x
string_length = len(string)
# print(string[0:2]) # ab
# print(string[2:4]) # ba

# print(string[0:2] + character + string[2:4]) # ab ba
# print(string[0:4] + character + string[4:8]) # test test
# print(string[0:1] + character + string[1:2]) # aa
# print(string[0:3] + character + string[3:6]) # abc abc

print(string[0:string_length // 2] + character + string[string_length // 2:string_length])

# abcba