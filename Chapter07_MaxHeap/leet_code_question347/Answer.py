from Chapter07_MaxHeap.priority_queue import PriorityQueue

def top_frequent(nums, k):
    map = dict()
    final_map = dict()
    for num in nums:
        if num in map.keys():
            map[num] += 1
        else:
            map[num] = 1

    for key, value in map.items():
        final_map[-1 * value] = key

    pq = PriorityQueue()

    for key in final_map.keys():
        if pq.get_Size() < k:
            pq.enqueue(key)
        else:
            if key < pq.get_Front():
                pq.dequeue()
                pq.enqueue(key)

    print(final_map[pq.dequeue()])
    res = []
    while not pq.is_Empty():
        e = pq.dequeue()
        res.append(final_map[e])
    return res

if __name__ == "__main__":
    nums = [2,3,3,5,5,5,5]

    print(top_frequent(nums,2))