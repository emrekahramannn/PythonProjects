"""
Given: 
Two DNA strings s and t (each of length at most 1 kbp).

Return: 
All locations of t as a substring of s.


Sample Dataset
GATATATGCATATACTT
ATAT

Sample Output
2 4 10
"""

def main(path):
    with open(path, mode="r") as fhandle:
        seq_mot = fhandle.readlines() # readlines return list
        seq = seq_mot[0][:-1] # do not include \n 
        if "\n" in seq_mot:
            motif = seq_mot[1][:-1] # do not include \n
        else:
            motif = seq_mot[1]

    seq_len = len(seq) 
    motif_len = len(motif)

    motif_starts = []

    i = 0 


    while i <= (seq_len - motif_len):
        if seq[i:i+motif_len] == motif:
            motif_starts.append(i+1)
        i += 1

    return " ".join(str(j) for j in motif_starts)


if __name__ == "__main__":
    test_or_full = input("Select a run mode: (T)est, (F)ull ").lower()
    
    test_sequence = r"Rosalind\datasets\motif.txt"
    full_seq = r"Rosalind\datasets\rosalind_subs.txt"

    if test_or_full in ["test", "t"]:
        result = main(test_sequence)
        assert result ==  "2 4 10", "Result does not match!"
        print("The result is matching, test is passed!")
    elif test_or_full in ["full", "f"]:
        result = main(full_seq)
        print(result)
    else:
        print("Invalid input! Try again.")