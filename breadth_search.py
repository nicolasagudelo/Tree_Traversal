from queue import Queue
from collections import deque

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        stack = deque()
        stack.append([self, 0])
        level_str = "\n"
        while len(stack) > 0:
            node, level = stack.pop()
      
            if level > 0:
                level_str += "| "*(level-1)+ "|-"
            level_str += str(node.value)
            level_str += "\n"
            level+=1
            for child in reversed(node.children):
                stack.append([child, level])

        return level_str
    

    def __repr__(self) -> str:
        return str(self.value)
  
    def add_child(self, node):
        self.children.append(node)
  
    def traverse(self):
        nodes = [self]      
        while nodes:
            current_node = nodes.pop(0)
            print(current_node.value)
            nodes += current_node.children

    def search(self, goal):
        frontier = Queue()
        root_node = self
        frontier.enqueue(root_node)
        while not frontier.is_empty():
            current_node = frontier.dequeue()
            if current_node.value == goal:
                print('Goal found')
                return current_node
            else:
                for child in current_node.children:
                    frontier.enqueue(child)
        print('{} is not in the tree'.format(goal))
        return 

    def search_path(self, goal):
        frontier = Queue()
        initial_path = [self]
        frontier.enqueue(initial_path)
        while not frontier.is_empty():
            current_path = frontier.dequeue()
            current_node = current_path[-1]
            if current_node.value == goal:
                print('Goal found')
                path =[]
                return current_path
            else:
                for child in current_node.children:
                    new_path = current_path.copy()
                    new_path.append(child)
                    frontier.enqueue(new_path)
        print('{} is not in the tree'.format(goal))
        return


sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")

sample_root_node.children = [docs, photos]
sample_root_node.children = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

print(sample_root_node)

goal_path = sample_root_node.search_path('Spot.jpg')

print(goal_path)

root_node = TreeNode(1)

root_node.add_child(TreeNode(2))
root_node.add_child(TreeNode(3))

root_node.children[0].add_child(TreeNode(4))
root_node.children[0].add_child(TreeNode(5))

root_node.children[1].add_child(TreeNode(6))
root_node.children[1].add_child(TreeNode(7))

# root_node.traverse()

print(root_node)

searched_node = root_node.search(7)

print(searched_node)

searched_path = root_node.search_path(7)

print(searched_path)