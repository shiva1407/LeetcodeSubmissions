class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i]!='*':
                st.append(s[i])
            else:
                if st:
                    st.pop()
        return ''.join(st)
                    
        