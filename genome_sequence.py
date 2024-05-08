#imports necessary libraries
import sys
from collections import defaultdict

filename = "test_sequences.txt"

#finda all substrings of k and their next substrings
def find_substrings(sequence, k):
    """
    finds all substrings of k and their next substrings.

    arguments:
        sequence(string): inputted sequence
        k(integer): the desired size of substrings

    returned:
        dictionary: a dictionary where keys are substrings and values are lists of subsequent substrings.
    """
    #creates a dictionary that stores the substrings and the subsequent substrings
    substrings = defaultdict(list)
    
    #goes over the sequence to find substrings
    for i in range(len(sequence) - k):
        #gets current substring
        substring = sequence[i:i + k]
        #gets the next substring
        next_substring = sequence[i + 1:i + k + 1]
        #adds the next substring to the list of subsequent substrings
        substrings[substring].append(next_substring)  
        
    return substrings

#finds all the possible substrings and their other substrings for all sequences
def find_all_substrings(filename, k):
    """
    -finds all possible substrings and their other substrings for all sequences

    arguments:
        filename(string): stores the sequence fragments file
        k(integer): the desired size of substrings 

    Returns:
        dictionary: A dictionary containing substrings and their subsequent substrings for all sequences.
    """
    #creates a dictionary to store all substrings and the other substrings for every sequence
    all_substrings = defaultdict(list)
    
    #reads the file
    with open(filename, 'r') as file:
        #an empty string in order to store the sequence
        sequence = ""  
        #goes over each line in the file
        for line in file:
            #indicates a new sequence
            if line.startswith(">"):
                #checks if theres a sequence stored from other iterations
                if sequence:
                    #finds all substrings for the desired sequence
                    substrings = find_substrings(sequence, k) 
                    #adds the substrings and their subsequent substrings to the dictionary
                    for key, value in substrings.items():
                        all_substrings[key].extend(value)
                #another empty string in order to stores others
                sequence = ""  
            else:
                #adds the line being used to the sequence
                sequence += line.strip()
        if sequence:
            #finds the substrings for prveious sequences
            substrings = find_substrings(sequence, k)  
            #adds the substrings and their subsequent substrings to the dictionary
            for key, value in substrings.items():
                all_substrings[key].extend(value)
                
    return all_substrings

#finds the smallest possible value of k where every substring has only one possible subsequent substring
def find_smallest_k(filename):
    """
    -finds the smallest value of k where every substring has only one possible subsequent substring.

    arguments:
        filename(string): stores the sequence fragments file

    returns:
        k(integer): smallest possible value of k 
    """
    #starts k of at  1
    k = 1
    #loops until the condition is met
    while True:  
        #gets all substrings for the k value
        substrings = find_all_substrings(filename, k)
        #creates a dictionary that stores the unique substrings for each substring
        unique_next_substrings = {substring: set(next_substrings) for substring, next_substrings in substrings.items()}
        #makes sure each unique substring occurs once
        if all(len(next_substrings) == 1 for next_substrings in unique_next_substrings.values()):
            #returns the k value
            return k
        #adds one to k after each loop  
        k += 1  

#defines a main funciton to run the script
def main(filename):
    """
    -this function finds the smallest k value and prints the output

    arguments:
        filename(string): stores the sequence fragments file
    """
        #check if the arguments are provided
    if len(sys.argv) != 2:
        print("Usage: py.test genome_sequence.py ../../shared/439539/reads.fa")
        sys.exit(1)
    #takes the "filename" from the command line
    filename = sys.argv[1]
    #finds the smallest k value
    smallest_k = find_smallest_k(filename)
    #prints the smallest k value
    print("Smallest value of k:", smallest_k)
    return smallest_k

#checks if the script is being run as the main program
if __name__ == "__main__":
    #calls the main function
    main(filename)  
