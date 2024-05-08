#import necessary libraries
import pytest
#get functions form main script
from genome_sequence import find_substrings, find_all_substrings, find_smallest_k, main

#tests find_substrings function
def test_find_substrings():
    #defines variable sequence
    sequence = "ATGTCTGTCTGAA"
    #defines different k values to test
    ks = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    #iterates over each k value
    for k in ks:
      #finds the substring for the provided one
      substrings = find_substrings(sequence, k)
      #makes sure substring exists
      assert substrings

#tests find_all_substrings function 
def test_find_all_substrings():
    #stores the file
    filename = "test_sequences.txt"
    #defines different k values to test
    ks = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    #iterates over each k value
    for k in ks:
      #finds all substring for the sequences within the file 
      all_substrings = find_all_substrings(filename, k)
      #makes sure the substrings exist
      assert all_substrings

#tests find_smallest_k function
def test_find_smallest_k():
    #stores the file
    filename = "test_sequences.txt"
    #calls main function
    smallest_k = main(filename)
    #checks if k is an integer
    assert isinstance(smallest_k, int)
    
#tests main function
#allows the script to test with different k values
@pytest.mark.parametrize("k", [2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_main(capsys, k):
    #stores the file
    filename = "test_sequences.txt"
    #calls main function
    smallest_k = main(filename)
    #gets the output of the main function
    captured = capsys.readouterr()
    #checks if the smallest k is in the caputered output
    assert "Smallest value of k:" in captured.out
    #also checks if k is an integer
    assert isinstance(smallest_k, int)

if __name__ == "__main__":
    pytest.main([__file__])
