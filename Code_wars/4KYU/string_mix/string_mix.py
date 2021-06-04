"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.
"""


def mix(s1, s2):
    l1, l2 = [l for l in s1 if l.isalpha() and l.islower()], [l for l in s2 if l.isalpha() and l.islower()]
    d1, d2 = {x: l1.count(x) for x in set(l1) if l1.count(x) > 1}, {x: l2.count(x) for x in set(l2) if l2.count(x) > 1}

    l_numerical = []
    l_equal = []

    for key in d1:
        if key in d2.keys():
            if d1[key] == d2[key]:
                l_equal.append(f'=:{key * d1[key]}')
            else:
                l_numerical.append(f'1:{key * d1[key]}') if d1[key] > d2[key] else l_numerical.append(f'2:{key * d2[key]}')
        else:
            l_numerical.append(f'1:{key * d1[key]}')

    for key in set(d2.keys()).difference(set(d1.keys())):
        l_numerical.append(f'2:{key * d2[key]}')

    return '/'.join(sorted(l_numerical + l_equal, key=lambda x: (-len(x), x, x[2:])))


print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"))
print(mix("Are they here", "yes, they are here"))