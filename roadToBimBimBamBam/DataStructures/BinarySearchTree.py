class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def new_node(item):
    temp = Node(item)
    temp.key = item
    temp.left = temp.right = None
    return temp


def insert(node: Node, key):
    if node is None:
        return new_node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    return node


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)


def preorder(root: Node):
    if root:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)


def postorder(root: Node):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')


def height(node: Node):
    if node is None:
        return 0
    else:
        left_depth = height(node.left)
        right_depth = height(node.right)

        if left_depth > right_depth:
            return left_depth + 1
        return right_depth + 1


def print_given_level(root, level):
    if root is None:
        return
    else:
        if level == 1:
            print(root.key, end=' ')
        elif level > 1:
            print_given_level(root.left, level - 1)
            print_given_level(root.right, level - 1)


def print_level_order(root):
    h = height(root)
    for i in range(1, h + 1):
        print_given_level(root, i)
        print()


def print_leaf_node(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.key)

    if root.left:
        print_leaf_node(root.left)
    if root.right:
        print_leaf_node(root.right)


def print_non_leaf_node(root):
    if root is None or (root.left is None and root.right is None):
        return

    if root.left is not None or root.right is not None:
        print(root.key, end=' ')

    print_non_leaf_node(root.left)
    print_non_leaf_node(root.right)


def right_view_util(root, level, max_level):
    if root is None:
        return

    if max_level[0] < level:
        print(root.key, end=' ')
        max_level[0] = level

    right_view_util(root.right, level + 1, max_level)
    right_view_util(root.left, level + 1, max_level)


def left_view_util(root, level, max_level):
    if root is None:
        return

    if max_level[0] < level:
        print(root.key, end=" ")
        max_level[0] = level

        # Recur for left and right subtrees
    left_view_util(root.left, level + 1, max_level)
    left_view_util(root.right, level + 1, max_level)


def right_view(root):
    max_level = [0]
    left_view_util(root, 1, max_level)


def min_value_node(node):
    current = node

    while current and current.left is not None:
        current = current.left

    return current


def delete_node(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.right
            root = None
            return None

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)
    return root


def min_value_node(root: Node):
    current = root
    while current and current.left is not None:
        current = current.left
    return current


def node_count(root):
    if root is None:
        return 0
    else:
        return node_count(root.left) + node_count(root.right) + 1


def empty_bst(root):
    if root is not None:
        empty_bst(root.left)
        empty_bst(root.right)
        print(root.key)
        del root


# Driver Code
if __name__ == '__main__':
    # Let us create following BST
    #          50
    #       /     \
    #     30      70
    #    /  \    /  \
    #  20   40  60   80
    root = None

    # Creating the BST
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    # Function Call

    empty_bst(root)
