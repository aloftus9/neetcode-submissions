# Finding an anagram is best using some sort of dict/ hash map
# Dictinary of dictionaries



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        result = dict()
        for s in strs:
            s_sorted = "".join(sorted(s))
            
            result[s_sorted] = result.get(s_sorted, []) + [s]

        result_list = []
        for value in result.values():
            result_list.append(value)

        return result_list





        

        
            

