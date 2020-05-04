"""
These are tests for miniprojects in.html and ip.html
"""

"""
A Mersenne number is any number that can be written as 2^p−1 for some  p.
For example, 3 is a Mersenne number (2^2−1). As is 31 (2^5−1).
We will see later on that it is easy to test if Mersenne numbers are prime.

Write a function that accepts an exponent p and returns the corresponding Mersenne number.

"""


def mersenne_number(p):
    return (2 ** p) - 1


def is_prime(number):
    if number <= 1:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True


def get_primes(starting, finishing):
    primes = []
    for number in range(starting, finishing):
        if is_prime(number):
            primes.append(number)
    return primes


def get_mersennes():
    mersennes = []
    for prime in get_primes(3, 65):
        mersennes.append(mersenne_number(prime))
    return mersennes


def lucas_lehmer_test(p):
    ll_list = [4]
    n = 4
    for s in range((p - 1)):
        n = ((n ** 2) - 2) % (2 ** p - 1)
        ll_list.append(n)
    return ll_list

# print(lucas_lehmer_test(17))

def lucas_lehmer_isprime(p):
    """
    A Mersenne number is prime if the position p-2 in the list is equal to 0
    :param p:
    :return:
    """
    ll_list = [4]
    n = 4
    for s in range((p - 1)):
        n = ((n ** 2) - 2) % (2 ** p - 1)
        ll_list.append(n)
    if ll_list[p - 2] == 0:
        return 1
    return 0


def ll_prime(p):
    primes = get_primes(3, 65)
    llp_list = []
    for prime in primes:
        llp_list.append(lucas_lehmer_isprime(prime))
    return list(zip(primes, llp_list))


def is_prime_fast(number):
    if (number % 2) == 0 and (number > 2) or number < 2:
        return False
    for odd in range(3, number, 2):
        if number % odd == 0:
            return False
    return True


def get_primes_fast(n):
    ll_primes = []
    for p in range(n + 1):
        if is_prime_fast(p):
            ll_primes.append(p)
    return ll_primes


"""
1. Generate a list of all numbers between 0 and N; mark the numbers 0 and 1 to be not prime
2. Starting with  p=2  (the first prime) mark all numbers of the form  np  where  n>1  and  np<=N  to be not prime
    (they can't be prime since they are multiples of 2!)
3. Find the smallest number greater than  p  which is not marked and set that equal to  p , then go back to step 2.
    Stop if there is no unmarked number greater than  pp  and less than  N+1N+1
    
* list_true = Make a list of true values of length  n+1  where the first two values are false
    (this corresponds with step 1 of the algorithm above)
* mark_false takes a list of booleans and a number  p . Mark all elements  2p,3p,...n false
    (this corresponds with step 2 of the algorithm above)
* find_next Find the smallest True element in a list which is greater than some p 
    (has index greater than  p  (this corresponds with step 3 of the algorithm above)
* prime_from_list Return indices of True values
"""


def list_true(n):
    list_ = [True] * (n + 1)
    list_[0] = False
    list_[1] = False
    return list_


def mark_false(bool_list, p):
    for n in range(2, len(bool_list)):
        mark = n * p
        if mark < len(bool_list):
            bool_list[mark] = False
    return bool_list


def find_next(bool_list, p):
    for n in range(p + 1, len(bool_list)):
        if bool_list[n]:
            return n
    return None


def prime_from_list(bool_list):
    ll = []
    for i in range(len(bool_list)):
        if bool_list[i]:
            ll.append(i)
    return ll


# assert len(list_true(20)) == 21
# assert list_true(20)[0] is False
# assert list_true(20)[1] is False
#
# assert mark_false(list_true(6), 2) == [False, False, True, True, False, True, False]
#
# assert find_next([True, True, True, True], 2) == 3
# assert find_next([True, True, True, False], 2) is None
#
# assert prime_from_list([False, False, True, True, False]) == [2, 3]
