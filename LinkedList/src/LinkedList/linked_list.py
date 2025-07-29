class ListNode():
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.root = None
    
    def append(self, value: int) -> None:
        if self.root is None:
            self.root = ListNode(value)
            return

        node = self.root
        while node.next:    
            node = node.next

        node.next = ListNode(value)
    
    def remove(self, value: int) -> None:
        if self.root is None:
            return
    
        if self.root.value == value:
            self.root = self.root.next
            return
        
        prev_node = self.root
        next_node = self.root.next
        while next_node:
            if next_node.value == value:
                prev_node.next = next_node.next
            
            prev_node = prev_node.next
            next_node = next_node.next
        
        return 

    def get_list(self) -> list[int]:
        node = self.root
        nums = []
        while node:
            nums.append(node.value)
            node = node.next
        
        return nums
    
    def __len__(self) -> int:
        length = 0
        node = self.root
        while node:
            length += 1
            node = node.next
        
        return length
    
    def contains(self, value: int) -> bool:
        node = self.root
        while node:
            if node.value == value:
                return True
            node = node.next

        return False

    def __contains__(self, value: int) -> bool:
        node = self.root
        while node:
            if node.value == value:
                return True
            node = node.next
        return False
    
    