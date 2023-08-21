# reverse a string and find whether it is a palindrome
input_str = 'Malayalam'
output_str = ''
for i in range(len(input_str)-1,-1,-1):
    output_str +=input_str[i]
if input_str.lower()==output_str.lower():
    print(input_str,' is a palindrome')
else:
    print(input_str,' is not a palindrome')
print(input_str,output_str)
