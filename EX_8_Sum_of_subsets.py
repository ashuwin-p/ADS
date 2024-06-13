def sum_of_subsets(S, target):
    def find(start, current_subset, current_sum):
        if current_sum == target:
            print(current_subset)
            return
        if current_sum > target:
            return
        for i in range(start, len(S)):
            find(i + 1, current_subset + [S[i]], current_sum + S[i])
    
    S.sort()
    find(0, [], 0)

S = [3, 7, 4, 9, 5, 2]
target = 9
sum_of_subsets(S, target)
