import pytest
from genome_sequence import find_substrings, find_all_substrings, find_smallest_k, main

# Test find_substrings function
def test_find_substrings():
    sequence = "ATGTCTGTCTGAA"
    k = 2
    substrings = find_substrings(sequence, k)
    assert substrings

# Test find_all_substrings function 
def test_find_all_substrings():
    filename = "test_sequences.txt"
    k = 2
    all_substrings = find_all_substrings(filename, k)
    assert all_substrings

# Test find_smallest_k function
def test_find_smallest_k():
    filename = "test_sequences.txt"
    smallest_k = main(filename)
    assert isinstance(smallest_k, int)
    
# Test main function
def test_main(capsys):
    filename = "test_sequences.txt"
    smallest_k = main(filename)
    captured = capsys.readouterr()
    assert "Smallest value of k:" in captured.out
    assert isinstance(smallest_k, int)

if __name__ == "__main__":
    pytest.main([__file__])
