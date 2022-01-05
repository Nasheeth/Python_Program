# Kevin and Stuart want to play the 'The Minion Game'.
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

def minion_game(string):
    h1 = 0
    h2 = 0
    vow = 'AEIOU'
    for i in range(len(s)):
        if s[i] not in vow:
            # h1 = h1 + len(s[i:])
            h1 = h1 + (len(s) - i)
        else:
            # h2 = h2 + len(s[i:])
            h2 = h2 + (len(s) - i)
    if h1 > h2:
        print('Stuart', h1)
    elif h1 < h2:
        print('Kevin', h2)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)