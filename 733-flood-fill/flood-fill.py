class Solution:
    from collections import deque
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        q=deque()
        act_color=image[sr][sc]
        if image[sr][sc]==color:
             return image       
        image[sr][sc]=color
        q.append((sr,sc))
        positions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            for _ in range(len(q)):
                left,right=q.popleft()
                for i,j in positions:
                    left_x=left+i
                    right_x=right+j
                    if left_x<0 or left_x==row or right_x==col or  right_x<0:
                        continue
                    if image[left_x][right_x]==color:
                    
                        continue
                    if image[left_x][right_x]==act_color:
                        image[left_x][right_x]=color
                        q.append((left_x,right_x))
        return image

            


        