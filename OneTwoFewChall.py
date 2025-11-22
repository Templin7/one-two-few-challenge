class CountMissingNums:
    """
    
    Hello,  this is my submission to the Weekly Challenge from the Slothbytes Newsletter
    I am in the process of familiarizing myself with Python for college and I have minimal coding experience with professional level code.
    There was an unexpected complication with my first for loop that I don't know the cause of but some offsets seem to fix the problem.
    FYI: Konami Code is an inside joke that simply refers to any code I used to locate errors that I want to keep for further changes
    
    """
    def countmissingnums(nums):
        """
        
        Finds missing numbers in an ordered number line counting linearly by taking first value & adding up to the last value
        and checking for matches. Adds missing numbers to a seperate list for potential use later. 
        Might retool later for use with an AI Agent or for another project in the future.
        
        Args:
            nums (list): a list of numbers that the program will find if there is any missing from a linear line from begining to end
        """
        nums.sort() # orders an unordered list because why not
        answer_key = []
        num_start = nums[0]
        num_end = nums[-1]
        output = 0
        missing_nums = []
        offset = 1 - num_start # forces the loop to start at the first number of the list by offsetting the jank

        # Problem: wants to start at one even if start is manually set; resolved, compensates using an offset
        for i in range(num_end + offset):
            answer_key.append(num_start + i)

        # Konami Code
        #key_start = answer_key[0]
        #key_end = answer_key[-1]
        #print(f'Answer Key: {answer_key}')
        #print(f'i = {i}')
        
        # ends code early if there is no difference to save on processing
        if answer_key == nums:
            print(f'Output: {output}')
            print('Missing nums: none')
            return None

        # Compares each number in the answer key to the original number line;
        # only runs if there is no match anywhere in number line
        for j in range(len(answer_key)):
            if not answer_key[j] in nums:
                output += 1
                missing_nums.append(answer_key[j])

        print(f'Output: {output}')
        print(f'Missing Numbers: {missing_nums}')

    countmissingnums([-2,1,4,5,6,8])
    #Output: 6
    #Missing Numbers: [-1, 0, 2, 3, 7]
    
    countmissingnums([3,5,9,10])
    #Output: 4
    #Missing Numbers: [4, 6, 7, 8]
    
    countmissingnums([1,3,5,6,7,8,10,11,12])
    #Output: 3
    #Missing Numbers: [2, 4, 9]
    
    countmissingnums([1,2,3,4,5])