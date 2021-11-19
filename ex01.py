# Minimum Cost to Hire K Workers
"""
There are n workers. 
 You are given two integer arrays quality and wage where 
 quality[i] is the quality of the ith worker and
 wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. 
To hire a group of k workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.

Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. 
Answers within 10-5 of the actual answer will be accepted.
"""

def solution(quality,wage):
    book = {}


    for q in range(len(quality)):
        book[quality[q]] = 



    pass

if __name__ == "__main__":
    quality = [3,1,10,10,1] 
    wage = [4,8,2,2,7]
    k = 3
    print(solution(quality,wage,k))
    pass