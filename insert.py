print("Enter 5 Elements of List:")
nums = []
for i in range(5):
 nums.insert(i, input())
print("Enter an Element to Insert at End: ")
elem = input()
nums.append(elem)
print("\nThe New List is: ")
print(nums) 
2