def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        temp = string[i:i+k]
        print(''.join(sorted(set(temp), key=temp.index)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
