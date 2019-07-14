import time

from Chapter14_HashTable.hash_table import HashTable

if __name__  == "__main__":

    with open('C:/Users/huangm/Desktop/Play-with-Data-Structures/Chapter06_Set_Map/shakes.txt', 'r') as f:
        content = f.read()
    words = content.split()

    start_time = time.time()
    hash_table = HashTable(M=131071)
    for word in words:
        print(word)
        if hash_table.contains(word):
            hash_table.set(word, hash_table.get(word) + 1)
        else:
            hash_table.add(word, 1)

    print("Total_words:", len(words))
    print("Unique words:", hash_table.get_size())
    print("Contains word 'they':", hash_table.contains('they'))
    print("HashTable Total time:{} seconds".format(time.time() - start_time))