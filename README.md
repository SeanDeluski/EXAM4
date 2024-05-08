Sean Deluski
Genome K-mer Analysis

This python script analyzes DNA sequences to find the smallest k value as well as looking for subsequent sequences.

genome_sequence.py and test_genome_sequence.py are the two scripts used in this analysis. 

Be sure to clone the repository to your computer.

This command can be helpful for using certain files: python genome_sequence.py <sequence_filename>

In order to run the tests use: pytest test_genome_sequence.py


File Structure:
genome_sequence.py = main script
test_genome_sequence.py = Test script

Functions:
find_substrings(sequence, k) = Finds all substrings of k and their subsequent substrings.
find_all_substrings = Finds all possible substring and their subsequent substrings.
find_smallest_k(filename) = Finds the smallest k value where each substring only has one subsequent string.
