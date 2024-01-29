"""
Problem
A recurrence relation is a way of defining the terms of a sequence with respect to 
the values of previous terms. In the case of Fibonacci's rabbits from the 
introduction, any given month will contain the rabbits that were alive the previous 
month, plus any new offspring. A key observation is that the number of offspring in 
any month is equal to the number of rabbits that were alive two months prior. As a 
result, if Fn represents the number of rabbit pairs alive after the n-th month, 
then we obtain the Fibonacci sequence having terms Fn that are defined by the 
recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). 
Although the sequence bears Fibonacci's name, it was known to Indian mathematicians 
over two millennia ago.

Given: 
Positive integers n<=40 and k<=5.

Return: 
The total number of rabbit pairs that will be present after nn months, if we begin
with 1 pair and in each generation, every pair of reproduction-age rabbits produces
a litter of kk rabbit pairs (instead of only 1 pair).

Sample Dataset:
5 3

Sample Output:
19
"""

def fibbonacci_rabbits(n, k):
    """
    Returns the number of rabbits present after n generations 
    with litters of k pairs
    """
    rabbits = [0,1]     # when starting 

    for i in range(n-1):
        rabbits[i%2] = rabbits[(i-1)%2] + k*rabbits[i%2]

    return rabbits[n%2]


def main(data_path):
    with open(data_path, "r",  encoding="utf8") as input_data:
        n, k = map(int, input_data.read().strip().split())

    return str(fibbonacci_rabbits(n, k))


if __name__ == "__main__":
    test_or_full = input("Select a run mode: (T)est, (F)ull ").lower()
    
    test_file = r"datasets/fibonacci_test.txt"
    full_file = r"datasets/rosalind_fib.txt"

    if test_or_full in ["test", "t"]:
        result = main(test_file)
        assert result ==  19, "Result does not match!"
        print("The result is matching, test is passed!")
    elif test_or_full in ["full", "f"]:
        result = main(full_file)
        print(result)
    else:
        print("Invalid input! Try again.")