#!/usr/bin/python3
'''
This is a function that determines the winner of a game based
on the number of prime numbers in a list of numbers.
'''


def isWinner(x, nums):
    '''
    x: int: the number of rounds
    nums: list of integers: a list of integers
    Returns: string: the name of the player that won the most rounds
    '''
    def is_prime(n):
        '''
        Helper function to check if a number is prime
        '''
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sieve_of_eratosthenes(n):
        '''
        Helper function to generate a list of prime numbers
        '''
        primes = []
        prime = [True for _ in range(n+1)]
        p = 2
        while (p * p <= n):
            if prime[p]:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        for p in range(2, n+1):
            if prime[p]:
                primes.append(p)
        return primes

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        # Since Maria always starts, if the number of prime
        # numbers is odd, she wins, otherwise Ben wins
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
