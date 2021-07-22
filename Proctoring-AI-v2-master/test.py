from math import sqrt
MAX = 100005
 
# Precompute Sieve, Prefix array, Suffix array
def precompute(prefix, suffix):
    prime = [True for i in range(MAX)]
 
    # Sieve of Eratosthenes
    k = int(sqrt(MAX))
    for i in range(2, k, 1):
        if (prime[i]):
            for j in range(i * i, MAX, i):
                prime[j] = False
 
    prefix[1] = 1
    suffix[MAX - 1] = int(1e9 + 7)
 
    # Precomputing Prefix array.
    for i in range(2, MAX, 1):
        if (prime[i]):
            prefix[i] = i
        else:
            prefix[i] = prefix[i - 1]
 
    # Precompute Suffix array.
    i = MAX - 2
    while(i > 1):
        if (prime[i]):
            suffix[i] = i
        else:
            suffix[i] = suffix[i + 1]
        i -= 1
 
# Function to solve each query
 
 
def query(prefix, suffix, L, R):
    if (prefix[R] < L or suffix[L] > R):
        return 0
    else:
        return prefix[R] - suffix[L]

def main():
    cases = int(input())
    prefix = [0 for i in range(MAX)]
    suffix = [0 for i in range(MAX)]
    precompute(prefix, suffix)

    for i in range(0,cases,1):
        l,r = int(input()),int(input())
        print(query(prefix,suffix,l,r))

main()