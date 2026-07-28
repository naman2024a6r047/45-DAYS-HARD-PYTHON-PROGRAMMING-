# your code goes here
n, days = map(int, input().split())
arr = list(map(int, input().split()))
l=1
h=sum(arr)
ans= -1
def check(mid):
	curr = 0
	day = 1
	for e in arr:
		if e > mid:
			return False
		elif curr + e <= mid:
			curr += e
		else:
			day += 1
			curr = e
  if day > days:
    return False
	return True

while l <= h:
	mid = (l + h) // 2
	if check(mid):
		ans = mid
		h = mid - 1
	else:
		l = mid + 1

print(ans)
