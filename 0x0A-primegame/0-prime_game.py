#!/usr/bin/python3
"""This kodule define the isWinner amd other helper functions
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def isWinner(x, nums):
    prime_cache = {}
    
    def can_win(n):
        if n in prime_cache:
            return prime_cache[n]
        
        primes = get_primes(n)
        if not primes:
            prime_cache[n] = False
            return False
        
        # Check if Maria can win
        for prime in primes:
            if not can_win(n - prime):
                prime_cache[n] = True
                return True
        
        # If Maria cannot win, then Ben wins
        prime_cache[n] = False
        return False
    
    maria_wins = 0
    for n in nums:
        if can_win(n):
            maria_wins += 1
    
    if maria_wins > x // 2:
        return "Maria"
    elif maria_wins < x // 2:
        return "Ben"
    else:
        return None

