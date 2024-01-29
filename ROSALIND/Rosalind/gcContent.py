"""
Given: 
At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: 
The ID of the string having the highest GC-content, followed by the GC-content of 
that string. Rosalind allows for a default error of 0.001 in all decimal answers 
unless otherwise stated; please see the note on absolute error below.

Sample Dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output:
Rosalind_0808
60.919540
"""


# import module
from Bio import SeqIO


def main(data_path):
    with open(data_path, 'r', encoding="utf8") as f:
        new_dict = {}
        # SeqIO.parse() takes a file handle (or filename) and format name, and returns a SeqRecord iterator.
        for i in SeqIO.parse(f, 'fasta'):
            sequence = i.seq
            gcContent = (sequence.count('G') + sequence.count('C'))/float(len(sequence)) * 100
            new_dict[i.id] = gcContent

    res_id = max(new_dict, key = new_dict.get)
    res_score =  f"{new_dict[res_id]:.6f}"

    return res_id, res_score


if __name__ == "__main__":
    test_or_full = input("Select a run mode: (T)est, (F)ull ").lower()
    
    test_file = r"datasets/gc_test.txt"
    full_file = r"datasets/rosalind_gc.txt"

    if test_or_full in ["test", "t"]:
        ID, score = main(test_file)
        print(ID, score, sep="\n")
        assert ID == 'Rosalind_0808' and score == "60.919540" , \
            "Resulting pair (id and score) does't match with expected result!"
        print("The result is matching, test is passed!")
    elif test_or_full in ["full", "f"]:
        ID, score = main(full_file)
        print(ID, score, sep="\n")
    else:
        print("Invalid input! Try again.")
