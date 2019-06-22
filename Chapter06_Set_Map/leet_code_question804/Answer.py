from Chapter06_Set_Map.bst_set import Set

def uniqueMorseRepresentations(words):
    codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    bst_set = Set()
    for word in words:
        res = []
        for i in word:
            print(ord(i))
            res.append(codes[ord(i) - ord('a')])
        bst_set.add(''.join(res))

    return bst_set.get_Size()

print(uniqueMorseRepresentations("abc"))