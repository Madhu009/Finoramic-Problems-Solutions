class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, root, totalsum):
        finallist = []
        clist = []
        finallist = self.R2L(root, totalsum, clist, finallist)
        return finallist

    def R2L(self, root, totalsum, clist, finallist):
        if (root.left is None) and (root.right is None):
            if totalsum == root.val:
                clist.append(root.val)
                currentR2L = clist[:]
                finallist.append(currentR2L)
                return finallist

        clist.append(root.val)

        if (root.left is not None):
            temp = clist[:]
            subsum = totalsum - root.val
            finallist = self.R2L(root.left, subsum, temp, finallist)

        if (root.right is not None):
            temp = clist[:]
            subsum = totalsum - root.val
            finallist = self.R2L(root.right, subsum, temp, finallist)

        return finallist