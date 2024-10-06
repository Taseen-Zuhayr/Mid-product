num =str(input("Enter a number here : "))
left = int(num[len(num)//2-1])
right = int(num[len(num)//2])
ans = left*right
print("The mid product is ",ans,".")