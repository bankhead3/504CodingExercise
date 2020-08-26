# 20200826 Armand
# this code counts characters and prints out a frequency for each type

# this function counts the characters in a string and returns a dictionary
def get_char_relfreq(inputString):
    b = dict()
    for c in inputString:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

inputString = 'ATCTGACGCGCGCCGC'
countDict = get_char_relfreq(inputString)
function2(countDict)
