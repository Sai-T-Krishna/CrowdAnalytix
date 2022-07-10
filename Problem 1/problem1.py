# base exception
class Error(Exception):
    pass

class DuplicateNumberFound(Error):
    pass

class ReverseClass(DuplicateNumberFound): 
    def reverse_func(self):

        # will check whether the given list contains duplicate numbers or not
        try:
            # must give an input
            N = int(input('Enter no. of elements: '))

            # creating a list from user inputs
            input_array = []
            for i in range(N):
                i = input("Enter the desired number:")

                # if the input is empty, it will pass, wont throw an error
                if i == '':
                    pass
                
                # else append the given inputs to the input_array
                else:
                    input_array.append(int(i))
            
            # loop through the input_array for any duplicates and raise an exception if duplicate number found
            for j in input_array:
                if j == '':
                    input_array.remove('')
                
                # if duplicate number found raise exception
                if input_array.count(j)>1:
                    raise DuplicateNumberFound
        
        # print the exception when a duplicate number is found
        except DuplicateNumberFound:
            print('Duplicate Number found at: {}'.format(input_array.index(j)+1))
        
        # if no duplicate number is found, reverse the given list
        else:
             print("Reversed list: ", input_array[::-1])

# function execution
if __name__=='__main__':
    a = ReverseClass()
    a.reverse_func()
