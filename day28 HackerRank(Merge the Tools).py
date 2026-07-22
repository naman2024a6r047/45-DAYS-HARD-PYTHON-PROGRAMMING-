def merge_the_tools(string, k):
    # your code goes here
    n= len(string)
    right=k
    left=0
    while right<=n:
        part = string[left:right]
        seen = set()
        answer = ""
        
        for ch in part:
            if ch not in seen:
                seen.add(ch)
                answer += ch
        
        print(answer)
        right+=k
        left+=k
      

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
