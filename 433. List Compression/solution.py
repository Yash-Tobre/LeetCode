class Solution:
    def compress(self, chars: List[str]) -> int:
        #initializing the list to be compressed
        compressed_list = [] 
        if len(chars)==1:
            return 1
        elif len(chars)==0:
            return 0

        else:
            i=0
            while i < len(chars):
                j=i
                count = 1
                while j < len(chars)-1 and chars[j]==chars[j+1]:
                    count += 1 
                    j+=1
                compressed_list.append(chars[i])
                if count >1:
                    if count >=10:
                        for each in list(str(count)):
                            compressed_list.append(each)
                    else:
                            compressed_list.append(str(count))
                i=j+1
                
            
            chars[:] = compressed_list

            return len(chars)


        
