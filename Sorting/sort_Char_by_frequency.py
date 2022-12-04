class Solution:
    def frequencySort(self, s: str) -> str:

        #[0-9]=10
        #[10-36]=26
        #[A---Z,a--z]
        arr = [(0,'')]*62
        for elem in s:
            if elem.islower():
                count,_=arr[ord(elem)-48-7-6]
                arr[ord(elem)-48-7-6] = (count+1,elem)
            elif elem.isupper():
                count,_=arr[ord(elem)-48-7]
                arr[ord(elem)-48-7] = (count+1,elem)
            else:
                count,_=arr[ord(elem)-48]
                arr[ord(elem)-48] = (count+1,elem)

        arr = sorted(arr,reverse = True)

        ans = ''
        for i in range(len(arr)):
            if arr[i][0]==0:
                continue
            else:
                ans  = ans+ arr[i][1]*arr[i][0]
        return ans

        




