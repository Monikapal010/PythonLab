class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Sort both lists
        list1.sort()
        list2.sort()
        
        # Merge the two sorted lists
        result = list1 + list2
        
        # Sort the final merged list
        result.sort()
        
        return result

# Create an instance of the Solution class
p = Solution()

# Define two lists
list1 = [3, 3, 46, 6]
list2 = [4, 5, 7, 2]

# Call the mergeTwoLists method and store the result
mergedlist = p.mergeTwoLists(list1, list2)

# Print the merged and sorted list
print(mergedlist)




