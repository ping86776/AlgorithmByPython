class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import string
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",
               ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        res = dict(zip(arr, mos))
        temp = ""
        list1 = []
        for i in words:
            for j in i:
                temp += res.get(j)
            list1.append(temp)
            temp = ""
        list2 = set(list1)
        print(string.ascii_lowercase)
        return len(list2)


if __name__ == '__main__':
    words = ["a"]
    Solution().uniqueMorseRepresentations(words)