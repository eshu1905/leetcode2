class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occ = {ch: i for i, ch in enumerate(s)}
        stack = []
        in_stack = set()
        
        for i, ch in enumerate(s):
            if ch in in_stack:
                continue
            while stack and ch < stack[-1] and i < last_occ[stack[-1]]:
                in_stack.remove(stack.pop())
            stack.append(ch)
            in_stack.add(ch)
        
        return "".join(stack)
            