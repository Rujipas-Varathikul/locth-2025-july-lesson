string = input() # abba
character = input() # c
string_length = len(string)
# a b b a
# 0 1 2 3

print(string[:(string_length // 2)]
      + character
      + string[(string_length // 2):])
