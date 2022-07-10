''' enter the number of tests we want to test '''
T = int(input('Enter no. of test cases:'))

''' take an empty list to append the user inputs and form a list '''
S = []
for i in range(T):
    i = input('Enter the input string:')
    S.append(i)

''' iterate through the list 'S' and perform the reverse operation '''
for item in S:
    '''
        1. first split the list -- item.split('-) i.e, tom-and-jerry will be ['tom','and','jerry']
        2. Now reverse the items in the list using slicing -- item.split('-)[::-1]
        3. Now join the elements using .join method and join with '-'
    
    '''
    print("Result: ", '-'.join(item.split('-')[::-1]))
