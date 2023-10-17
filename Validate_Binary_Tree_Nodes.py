class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild):
        def findRoot(): # to find the root node
            children = set(leftChild)|set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1 # -1 means all nodes have their parents

        root = findRoot()
        if root == -1:
            return False
        seen = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node],rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False
                    stack.append(child)
                    seen.add(child)
        return len(seen) == n

n=4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]
obj = Solution()
print(obj.validateBinaryTreeNodes(n,leftChild,rightChild))