# Given weights and values of n items, put these items in a knapsack/backpack of capacity W to get the maximum total value in the knapsack/backpack.
# In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.

def knapsack(W, wt, val, n):
    max_value = [0 for i in range(W+1)]
    
    for i in range(n):
        temp_max = val[i]
        temp_weight = wt[i]
        max_value[temp_weight] = temp_max
        for j in range(i+1, n):
            if wt[i] + wt[j] <= W: # check weight first
                if val[i] + val[j] > val[i]:
                    temp_max = val[i] + val[j]
                    temp_weight = wt[i] + wt[j]
                    max_value[temp_weight] = temp_max
            if wt[i] + max_value.index(max(max_value)) <= W:
                if val[i] + max(max_value) > val[i] and val[i] != max(max_value):
                    temp_max = val[i] + max(max_value)
                    temp_weight = wt[i] + max_value.index(max(max_value))
                    max_value[temp_weight] = temp_max

    return max(max_value)
 
val = [int(x) for x in input("Enter values of objects (seperated by spaces): ").split()]
wt = [int(x) for x in input("Enter weights of objects (seperated by spaces): ").split()]
W = int(input("Enter weight capacity of knapsack: "))
n = len(val)
print("Total value you can carry is: " + str(knapsack(W, wt, val, n)))