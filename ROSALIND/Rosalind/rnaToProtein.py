"""
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the 
English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are
constructed from these 20 symbols. Henceforth, the term genetic string will 
incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons 
into the amino acid alphabet.


Given: 
An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: 
The protein string encoded by s.


Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output
MAMAPRTEINSTRING
"""

from Bio.Seq import Seq

def rna2protein(file_path):
    with open(file_path, "r") as fhandle:
        seq = fhandle.read().strip()

    rna_seq = Seq(seq)
    return rna_seq.translate(stop_symbol="")


if __name__ == "__main__":
    test_or_full = input("Select a run mode: (T)est, (F)ull ").lower()
    
    test_sequence = r"Rosalind\datasets\rna2protein_test.txt"
    full_seq = r"Rosalind\datasets\rosalind_prot.txt"

    if test_or_full in ["test", "t"]:
        result = rna2protein(test_sequence)
        assert result ==  "MAMAPRTEINSTRING", "Result does not match!"
        print("The result is matching, test is passed!")
    elif test_or_full in ["full", "f"]:
        result = rna2protein(full_seq)
        print(result)
    else:
        print("Invalid input! Try again.")