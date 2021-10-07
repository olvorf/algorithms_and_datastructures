# python3
import sys


def ibwt3(row_number, text):

    def row(row_number):
        permutation = sorted((t, i) for i, t in enumerate(text))
        for _ in text:
            t, row_number = permutation[row_number]
            yield t
    return ''.join(row(row_number))

'''
slow version


def InverseBWT(text):
    
    matrix = [''] * len(text)
    output = ''
    for _ in text:
        matrix = sorted(i+j for i,j in zip(text,matrix))
    #matrix = str(matrix).strip("[]")
    output = matrix[0]
    dollar = output[0]
    r_text = output[1:]
    l = []
    l.append(r_text)
    l.append(dollar)

    return l
'''
    



if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    #l = InverseBWT(bwt)
    l = ibwt3(0,bwt)
    m = []
    m.append(l[1:])
    m.append(l[0])
    print(''.join(m))