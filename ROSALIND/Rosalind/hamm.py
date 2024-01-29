"""
Given: 
Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: 
The Hamming distance d_h(s,t).

Sample Dataset:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output:
7
"""


def hamming_distance(seq1,seq2):
    """Calculate the point mutations"""
    if len(seq1) != len(seq2):
        raise ValueError("Sequences have different lengths")
    else:
        return sum(b1 != b2 for b1, b2 in zip(seq1, seq2))
    


def main(data_path):
    with open(data_path, 'r') as f:
        all_seq = f.readlines()
        seq1 = all_seq[0][:-1] # to not include \n
        if '\n' in all_seq[1]:
            seq2 = all_seq[1][:-1]
        else:
            seq2 = all_seq[1]
    return hamming_distance(seq1, seq2)



if __name__ == "__main__":
    test_or_full = input("Select a run mode: (T)est, (F)ull ").lower()
    
    test_file = r"datasets/hamm_test.txt"
    full_file = r"datasets/rosalind_hamm.txt"

    if test_or_full in ["test", "t"]:
        result = main(test_file)
        assert result ==  7, "Result does not match!"
        print("The result is matching, test is passed!")
    elif test_or_full in ["full", "f"]:
        result = main(full_file)
        print(result)
    else:
        print("Invalid input! Try again.")





"""
Easy to understand function as an alternative

def hamming_distance(seq1, seq2):
    
    index = 0
    mutations = 0

    if len(seq1) != len(seq2):
        raise ValueError("Sequences have different lengths")
    else:
        for base in seq1:
            if base != seq2[index]:
                mutations += 1
            index +=1
    return mutations
    
"""