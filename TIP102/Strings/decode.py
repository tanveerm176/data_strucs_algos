def decode(message_file):
    #create dictionary for number line pairs
    line_word_pairs = {}

    #read the message file as line by line
    with open(message_file, 'r') as input_file:
        for line in input_file:
           number_word_list = line.strip().split(" ")
           number = int(number_word_list[0])
           line = number_word_list[1]
           line_word_pairs[number] = line
    
    #determine which lines to use from the pyramid
    lines_to_use = []
    current_sum = 0 
    current_line = 1 #start at the first line
    while current_sum + current_line in line_word_pairs:
        current_sum += current_line
        lines_to_use.append(current_sum)
        current_line = current_line +1
    
    decoded_msg = ' '.join(line_word_pairs[line] for line in lines_to_use)
    return decoded_msg

input_file = 'Leetcode_Strings/coding_qual_input.txt'
print(decode(input_file))
