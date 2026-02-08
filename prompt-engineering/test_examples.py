#1
def sort_list(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#2
def build_sentence(words):
    res = ''
    for w in words:
        res = res + w + ' '
    return res

#3
def find_users(target_ids, all_users):
    # all_users is a list of dicts like {'id': 1, 'name': 'x'}
    found = []
    for uid in target_ids:
        for u in all_users:
            if u['id'] == uid:
                found.append(u)
    return found

#4
def is_prime_sum(n):
    primes = []
    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return sum(primes)

#5
total = 0

def add_to_total(nums):
    global total
    for x in nums:
        total += x
    return total
