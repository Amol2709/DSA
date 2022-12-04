class Solution:
    def dividePlayers(self, skill) -> int:
        # leetcode: 2491
        # 1 2 2 5
        n = len(skill)
        total_sum = sum(skill)
        
        team = n//2
        
        if total_sum%team!=0:
            return -1
        
        target = total_sum//team
        skill.sort()
        p1,p2 = 0,n-1
        ans = 0
        while(p1<p2):
            if skill[p1]+skill[p2]!=target:
                return -1
            
            ans = ans + (skill[p1]*skill[p2])
            p1+=1
            p2-=1
        return ans