class TreeNode:

    def __init__(self, key: int, val: int, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:

    root: TreeNode | None
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        
        def _insert(root: TreeNode | None, key: int, val: int) -> TreeNode:
            if not root:
                return TreeNode(key=key, val=val)

            if key < root.key:
                root.left = _insert(root.left, key, val)
            elif key > root.key:
                root.right = _insert(root.right, key, val)
            else:
                root.val = val
            return root

        self.root = _insert(self.root, key, val)

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        minNode = self._findMin(self.root)
        return minNode.val if minNode else -1

    def _findMin(self, root: TreeNode | None) -> TreeNode | None:
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur

    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val if cur else -1

    def remove(self, key: int) -> None:
        
        def _remove(root: TreeNode | None, key: int) -> TreeNode | None:
            if not root:
                return None
            
            if key < root.key:
                root.left = _remove(root.left, key)
            elif key > root.key:
                root.right = _remove(root.right, key)
            else:
                if not root.right:
                    root = root.left
                elif not root.left:
                    root = root.right
                else:
                    minNode: TreeNode = self._findMin(root.right)
                    root.key = minNode.key
                    root.val = minNode.val
                    root.right = _remove(root.right, minNode.key)
                    
            return root

        self.root = _remove(self.root, key)


    def getInorderKeys(self) -> List[int]:
        result: list[int] = []
        
        def _inorder(root: TreeNode | None):
            if not root:
                return

            _inorder(root.left)
            result.append(root.key)
            _inorder(root.right)

        _inorder(self.root)
        
        return result

        
        


