n=[]
s=[]
total=0
avg=0
amount=int(input("請輸入班上總人數: "))
for _ in range(amount):
    name=input("請輸入名字: ")
    score=int(input("請輸入分數: "))
    n.append(name)
    s.append(score)
print (s)

for m in range(amount):
    total=total+s[m]
avg=total/amount
print("平均是",avg)

highest=0
lowest=99999999
for k in s:
    if k>highest:
        highest=k
print("最高分為",highest)

for j in s:
    if j<lowest:
        lowest=j
print("最低分為",lowest)
    
    
    


