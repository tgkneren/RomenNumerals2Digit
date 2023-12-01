roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def converter(index):
    sum=0
    for i in range(len(index)-1):
        if index[i] < index[i+1]:
            sum = sum + (index[i+1] - index[i])
        elif index[i] >= index[i+1]:
            sum = sum + index[i]
    if index[-2] >= index[-1]:
        sum = sum+index[-1]
    print(sum)
while True:
    input_array = []
    user_input = input("Enter a romen numeral\n ").upper()
    input_array = []
    for harf in user_input:
        if harf in roman_numerals:
            input_array.append(roman_numerals[harf])
    converter(input_array)
