"""
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the 
symbols of s, then taking the complement of each symbol (e.g., the reverse 
complement of "GTCA" is "TGAC").

Given: 
A DNA string s of length at most 1000 bp.

Return: 
The reverse complement sc of s.

Sample Dataset
AAAACCCGGT

Sample Output
ACCGGGTTTT
"""

def reverse_complement(seq):
    seq = seq.upper() # turn the all string into uppercase
    seq = seq[::-1]   # reverse the string for further manipulation

    # complement base for each base
    complements = {"A": "T", "C": "G", "G": "C", "T": "A"}

    bases = list(seq) # turns the string into a list (each char in a string is now a list element)

    new_bases = []
    for i in bases:
        new_bases.append(complements.get(i))
    
    return "".join(new_bases)


def main(data_path):
    with open(data_path, mode="r", encoding="utf8") as seq:
        seq = seq.read().strip()
    transcribed_seq = reverse_complement(seq)
    return transcribed_seq





if __name__ == '__main__':
    test_or_full = input("Select a run mode: (T)est, (F)ull ").lower()
    
    test_sequence = "AAAACCCGGT"
    full_seq = r"datasets/rosalind_revc.txt"

    if test_or_full in ["test", "t"]:
        result = reverse_complement(test_sequence)
        assert result ==  "ACCGGGTTTT", "Result does not match!"
        print("The result is matching, test is passed!")
    elif test_or_full in ["full", "f"]:
        result = main(full_seq)
        print(result)
    else:
        print("Invalid input! Try again.")
