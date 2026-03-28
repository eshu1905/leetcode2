from collections import deque

class Solution(object):
    def distanceK(self, root, target, k):
        if not root:
            return []

        # 🔹 Step 1: Build parent map
        parent = {}

        def mark_parent(node, par):
            if not node:
                return
            parent[node] = par
            mark_parent(node.left, node)
            mark_parent(node.right, node)

        mark_parent(root, None)

        # 🔹 Step 2: BFS from target
        def distance(node, k):
            ans = []
            visited = set()

            q = deque([(node, 0)])
            visited.add(node)

            while q:
                ele, dist = q.popleft()

                if dist == k:
                    ans.append(ele.val)

                if dist > k:
                    break

                for nei in (ele.left, ele.right, parent[ele]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append((nei, dist + 1))

            return ans

        return distance(target, k)
            
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        