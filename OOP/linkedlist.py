class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?""" """O(n) input dependent loop"""
        # TODO: Loop through all nodes and count one for each
        count = 0
        current_node = self.head

        while current_node is not None:
            count = count + 1


            current_node = current_node.next




        return count

        # for i in self.items():
        #     count += 1
        # return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?""" """O(1)"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

        new_node = Node(item)

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node


            self.tail = new_node


        return new_node



    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node


            # self.head = new_node


        return new_node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        current_node = self.head
        while current_node is not None:
        # TODO: Check if node's data satisfies given quality function
            if quality(current_node.data):
                return current_node.data

            current_node = current_node.next
        return None  #maybe return None

        # while item is not None:
        #     if item == quality:
        #         return True
        #     else:
        #         return False

    # def find_node():

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        """Huge shout out to Sam for helping us with this functing"""

        if self.is_empty(): #if is_empty is True
            raise ValueError('Item not found: {}'.format(item)) #The list is empty and throw error
            return

        currentNode = self.head

        if currentNode.data == item: #if head has the item
            self.head = currentNode.next #if head has next... assign next as new head
            if currentNode.next == None: #head is the last item... set self.tail to none
                self.tail = None
            return
        prev = None
        while currentNode != None: #loop until we reach tail
            print("Current node =", currentNode)
            if currentNode.data == item: #if node's data is the item... found!
                if currentNode.next == None: #if currentNode is the tail because it has no next...
                    self.tail = prev #prev node will now be the new tail
                prev.next = currentNode.next #DELETE currentNode by removing prev's next (reference) to currentNode's next
                return
            # TODO: Update previous node to skip around node with matching data
            prev = currentNode #if currentNode's data is not item,
            currentNode = currentNode.next #keep going til it reach the tail
            print("Current.next = ", currentNode)
        # TODO: Otherwise raise error to tell user that delete has failed
        raise ValueError('Item not found: {}'.format(item))



    # def delete(self, item):
    #     """Delete the given item from this linked list, or raise ValueError.
    #     TODO: Best case running time: O(???) Why and under what conditions?
    #     TODO: Worst case running time: O(???) Why and under what conditions?"""
    #     # TODO: Loop through all nodes to find one whose data matches given item
    #     if self.is_empty():
    #         raise ValueError('Item not found {}'.format(item))
    #
    #     current_node = self.head.next
    #     previous_node = self.head
    #
    #     if self.head.data == item:
    #         self.head = self.head.next
    #         return item
    #
    #     while current_node is not None: #self.tail:
    #         if current_node.next == None:
    #             if current_node == self.tail:
    #                 self.tail = previous_node
    #             # previous_node.next = None
    #             return
    #         # TODO: Update previous node to skip around node with matching data
    #
    #             previous_node.next = current_node.next
    #             return
    #     # TODO: Otherwise raise error to tell user that delete has failed
    #
    #         previous_node = previous_node.next
    #         current_node = current_node.next
    #
    #         raise ValueError('Item not found: {}'.format(item))
    #     # Hint: raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
