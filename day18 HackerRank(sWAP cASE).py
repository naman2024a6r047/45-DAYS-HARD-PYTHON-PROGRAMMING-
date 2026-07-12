def swap_case(s):
    res=""
    for w in s:
        if w.upper()==w:
            res+=w.lower()
        else:
            res+=w.upper()
    return res


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
