# python3
import sys

def BWT(text):
    matrix = [text]
    for i in range(1,len(text)):
        text = text[-1] + text[:-1]
        matrix.append(text)
        i += 1
    
    sorted_matrix = sorted(matrix)
    
    last_element = ''
    for word in sorted_matrix:
        last_element += word[-1] 
    return last_element


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))