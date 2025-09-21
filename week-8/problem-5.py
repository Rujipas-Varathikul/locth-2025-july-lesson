# loop by index
# input 'hello'
answer = '' # '' + 'h' + '_' => 'h_'

string = input()

for character in string:
    answer = answer + character + '_'

# answer = '' + 'h' + '_'
# answer = 'h_'
# answer = 'h_' + 'e' + '_'
# answer = 'h_e_'

print(answer[:-1]) # answer 'h_e_l_l_o'