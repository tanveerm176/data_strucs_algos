def twice_occurence(s):
    
    min_index = len(s)

    print(f'string = {list(s)}')

    for i in range(len(s)):

        print(f'i = {i}')

        for j in range(i+1, len(s)):

            print(f'j = {j} and min index = {min_index}')

            if s[i]==s[j]:

                print(f's[i] = {s[i]} and s[j] = {s[j]}')
                
                if j < min_index:

                    min_index = j

    return s[min_index]

print(twice_occurence("abcdd"))