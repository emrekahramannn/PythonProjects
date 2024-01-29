"""
PROBLEM:
A string is simply an ordered collection of symbols selected from some alphabet and
formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: 
A DNA string s of length at most 1000 nt.

Return: 
Four integers (separated by spaces) counting the respective number of times that 
the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output
20 12 17 21
"""


def count_nucleotides(seq):
    """function to count nucleotides in given sequence"""
    seq = seq.upper()
    return seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")


def main(data_path):
    """Open the file and count the nucleotides in the seq.
        and return the number of nucleotides (A C G T)"""
    
    with open(data_path, "r") as seq:
        seq = seq.read().strip()

    output = count_nucleotides(seq) # returns a tuple
    
    return ' '.join([str(i) for i in output]) # .join works on str objects, we need to convert the int to str w/ str method


if __name__ == "__main__":
    test_or_full = input("Select a run mode: (T)est, (F)ull ").lower()
    
    test_sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    full_seq = r"datasets/rosalind_dna.txt"

    if test_or_full in ["test", "t"]:
        result = count_nucleotides(test_sequence)
        assert result ==  (20, 12, 17, 21), "Result does not match!"
        print("The result is matching, test is passed!")
    elif test_or_full in ["full", "f"]:
        result = main(full_seq)
        print(result)
    else:
        print("Invalid input! Try again.")
