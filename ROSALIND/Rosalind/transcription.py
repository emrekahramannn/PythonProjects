"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string 
u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: 
A DNA string t having length at most 1000 nt.

Return: 
The transcribed RNA string of t.


Sample Dataset
GATGGAACTTGACTACGTAAATT

Sample Output
GAUGGAACUUGACUACGUAAAUU
"""


def transcribe(seq):
    """
    This function changes all the appearances of T in the seq to U
    """
    seq = seq.upper() 
    RNA = ['U' if base == 'T' else base for base in seq]
    return "".join(RNA)

def main(data_path):
    with open(data_path, "r") as seq:
        seq = seq.read().strip()
    return transcribe(seq)
    

if __name__ == "__main__":
    test_or_full = input("Select a run mode: (T)est, (F)ull ").lower()
    
    test_sequence = "GATGGAACTTGACTACGTAAATT"
    full_seq = r"datasets/rosalind_rna.txt"

    if test_or_full in ["test", "t"]:
        result = transcribe(test_sequence)
        assert result ==  "GAUGGAACUUGACUACGUAAAUU", "Result does not match!"
        print("The result is matching, test is passed!")
    elif test_or_full in ["full", "f"]:
        result = main(full_seq)
        print(result)
    else:
        print("Invalid input! Try again.")



"""
Instead of using list comprehension we can use str.replace() method

def transcribe(seq):
    seq = seq.upper()
    return seq.replace("T", "U")


or instead of using list, we can use strings to hold the information

def transcribe(seq):
    seq = seq.upper()
    transcribed_seq = ""

    for n in seq:
        if n == "T":
            transcribed_seq += "U"
        else:
            transcribed_seq += n
    
    return transcribed_seq
"""