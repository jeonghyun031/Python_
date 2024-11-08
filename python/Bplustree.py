class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(True)
        self.t = t
    
    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            new_node = BPlusTreeNode(False)
            new_node.children.append(self.root)
            self.root = new_node
            self.split_child(new_node, 0)
            self._insert_non_full(new_node, key)
        else:
            self._insert_non_full(root, key)

    def split_child(self, parent, index):
        t = self.t
        child = parent.children[index]
        new_child = BPlusTreeNode(child.leaf)
        
        parent.keys.insert(index, child.keys[t - 1])
        parent.children.insert(index + 1, new_child)
        
        new_child.keys = child.keys[t:]
        child.keys = child.keys[:t - 1]
        
        if not child.leaf:
            new_child.children = child.children[t:]
            child.children = child.children[:t]

    def _insert_non_full(self, node, key):
        if node.leaf:
            index = 0
            while index < len(node.keys) and key > node.keys[index]:
                index += 1
            node.keys.insert(index, key)
        else:
            index = 0
            while index < len(node.keys) and key > node.keys[index]:
                index += 1
            if len(node.children[index].keys) == (2 * self.t - 1):
                self.split_child(node, index)
                if key > node.keys[index]:
                    index += 1
            self._insert_non_full(node.children[index], key)

    def print_tree(self, node, level=0):
        print("Level", level, "Keys:", node.keys)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

bptree = BPlusTree(t=3)
print("차수가 3인 B+트리")
print("키 값을 입력하시오 (enter를 눌러 종료합니다.):")
while True:
    input_key = input("Enter key: ")
    if input_key == "":
        break
    try:
        key = int(input_key)
        bptree.insert(key)
    except ValueError:
        print("정수만 입력하시오")

print("\n최종 B+트리 구조")
bptree.print_tree(bptree.root)
