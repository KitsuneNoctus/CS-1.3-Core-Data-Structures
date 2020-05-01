# Linked List Stack
def push(self, item):
    """Insert the given item on the top of this stack"""
    self.list.prepend(item)

def peek(self):
    """Return the item on the top of this stack without removing it"""
    if self.is_empty() == True:
        return None

    return self.list.head.data

def pop(self):
    """Remove and return the item on the top of this stack"""
    if self.is_empty() == True:
        raise ValueError

    top_data = self.list.head.data
    self.list.delete(self.list.head.data)

    return top_data

# Dynmic Array Stack
def push(self, item):
    """Insert the given item on the top of this stack"""
    self.list.insert(0,item)

def peek(self):
    """Return the item on the top of this stack without removing it"""
    if self.is_empty() == True:
        return None
    return self.list[0]

def pop(self):
    """Remove and return the item on the top of this stack"""
    if self.is_empty() == True:
        raise ValueError

    data = self.list[0]
    self.list.pop(0)
    return data

# Linked List Queue
def enqueue(self, item):
    """Insert the given item at the back of this queue."""
    self.list.append(item)

def front(self):
    """Return the item at the front of this queue without removing it,"""
    if self.is_empty() == True:
        return None
    return self.list.head.data

def dequeue(self):
    """Remove and return the item at the front of this queue"""
    if self.is_empty() == True:
        raise ValueError

    head_data = self.front()

    self.list.delete(self.list.get_at_index(0))

    return head_data

# Dynmic Array Queue
def enqueue(self, item):
    """Insert the given item at the back of this queue."""
    self.list.append(item)

def front(self):
    """Return the item at the front of this queue without removing it"""
    if self.is_empty() == True:
        return None
    return self.list[0]

def dequeue(self):
    """Remove and return the item at the front of this queue"""
    if self.is_empty() == True:
        raise ValueError
    head_data = self.list[0]
    self.list.pop(0)
    return head_data
