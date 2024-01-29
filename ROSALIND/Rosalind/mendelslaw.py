"""
Given: 
Three positive integers k, m, and n, representing a population containing 
k+m+n organisms: k individuals are homozygous dominant for a factor, m are 
heterozygous, and n are homozygous recessive.

Return: 
The probability that two randomly selected mating organisms will produce an 
individual possessing a dominant allele (and thus displaying the dominant phenotype). 
Assume that any two organisms can mate.

Sample Dataset
2 2 2

Sample Output
0.78333
"""

def main(path):
    with open(path, mode="r", encoding="utf-8") as fhandle:
        k,m,n = map(int, fhandle.read().strip().split())

        chances = ((k*k - k) + 2*(k*m) + 2*(k*n) + (.75*(m*m - m)) + 2*(.5*m*n))/ ((k + m + n) * (k + m + n - 1))
        return float("{:.5f}".format(chances))
    


if __name__ == "__main__":

    test_or_full = input("Select a run mode: (T)est, (F)ull ").lower()
    
    test_file = r"datasets/mendels.txt"
    full_file = r"datasets/rosalind_iprb.txt"

    if test_or_full in ["test", "t"]:
        result = main(test_file)
        assert result ==  0.78333, "Result does not match!"
        print("The result is matching, test is passed!")
    elif test_or_full in ["full", "f"]:
        result = main(full_file)
        print(result)
    else:
        print("Invalid input! Try again.")
