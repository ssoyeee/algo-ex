
# Python program to find minimum
# operations required to
# make two numbers equal
import math
 
# Function to return the
# minimum operations required
def minOperations(A, B):
 
    # Keeping B always greater
    if (A > B): swap(A, B)
 
    # Reduce B such that
    # gcd(A, B) becomes 1.
    B = B // math.gcd(A, B)
 
    return B - 1
 
# Driver code
A = 22
B = 75
 
print(minOperations(A, B))