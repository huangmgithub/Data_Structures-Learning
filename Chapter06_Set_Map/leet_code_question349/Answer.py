from Chapter06_Set_Map.linkedlist_set import LinkedListSet

def intersection(nums1, nums2):
    linked_list_set = LinkedListSet()
    res_list = []
    for i in nums1:
        linked_list_set.add(i)
    for i in nums2:
        if linked_list_set.contains(i):
            res_list.append(i)
            linked_list_set.remove(i)

    return res_list


nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))