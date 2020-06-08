def threesum(nums):
    number=[]
    nums_a=sorted(nums)
    nums_b = nums_a
    for i in nums_a:
        a=i
        del nums_b[0]
        nums_c=nums_b
        for j in nums_b:
            b=j
            del nums_c[0]
            for k in nums_c:
                c=k
                L=sorted([a,b,c])
                if a+b+c==0 and L not in number:
                 number.append(L)
    return number
print(threesum([3,0,-1,-2]))