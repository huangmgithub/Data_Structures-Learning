from Chapter06_Set_Map.linkedlist_map import LinkedListMap

def intersect(nums1, nums2):
    map = LinkedListMap()
    res = []
    for i in nums1:
        if not map.contains(i):
            map.add(i, 1)
        else:
            map.set(i, map.get(i) + 1)
    for i in nums2:
        if map.contains(i):
            res.append(i)
            map.set(i, map.get(i) - 1)
            if map.get(i) == 0:  #重复值为0则删除
                map.remove(i)
    return res

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersect(nums1, nums2))

