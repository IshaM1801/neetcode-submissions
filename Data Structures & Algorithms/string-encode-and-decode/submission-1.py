class Solution:

    def encode(self, strs: List[str]) -> str:
        i=1
        l=0
        e={0:0}
        encoded_str=""
        for str in strs:
            encoded_str+=str
            encoded_str+="ü"
        print (encoded_str)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_str=[]
        st=""
        for i in s:
        
            if i == 'ü':
                decoded_str.append(st)
                st=""
                
            else:
                st+=i
            
        return decoded_str



