num = [1,2,3,4,5]
target = 5
mid = int(len(num)/ 2)

if num[mid]  == target:
        print("found")
elif num[mid] < target:
        lst = [x for x in range(mid,len(num)+1)]

        print(lst)