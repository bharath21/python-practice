n,k=map(int,raw_input().split())
#if isinstance(n,int):
#    print("yes")
li=[]
li = map(int,raw_input().split())
#try:
#    assert (len(li) == n)
#except AssertionError:
#    print ("list count is not n")
count_li=[]
for i in range(k):
    count_li.append(0)
for i in range(n):
    count_li[li[i]%k] += 1
rem_li=[]
rem_li = [i%k for i in li]
final_li = []
final_count = 0
for i in range(1,k/2+1):
    if (i != k-i):
        if(count_li[i] > count_li[k-i]):
            final_count += count_li[i]

        else:
            final_count += count_li[k-i]
            
if (count_li[0] > 0):
    final_count += 1
    
if(k%2 == 0 and count_li[k/2] > 0):
    final_count += 1

print (final_count)
        
    