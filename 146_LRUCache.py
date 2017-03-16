'''
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
class ListNode(object):
    def __init__(self, x, prev):
        self.val = x
        self.prev = prev
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.memo = {}
        self.head, self.tail = self.ListNode(0, 0), self.ListNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.cnt = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print("get key:", key)
        copy = self.head
        if key not in self.memo:
            return -1
        keyNode = self.memo[key]
        res = keyNode.val[1]
        if key == self.curr.val[0]: # res if last touched node
            return res
        copy = self.head.next
        while copy and copy.next:
            print("link list get", copy.val, copy.prev.val, copy.next.val)
            copy = copy.next
        pre, after = keyNode.prev, keyNode.next
        pre.next, after.prev = after, pre
        #keyNode.prev.next, keyNode.next.prev = keyNode.next, keyNode.prev # skip this key
        self.tail.prev = ListNode((key, res), self.curr) # add to end
        self. = self.curr.next
        self.curr.next = ListNode(0, self.curr) # add dummy node to end
        self.memo[key] = self.curr # update record {key: node in memo}
        print("get new key:", key, self.curr.val, self.curr.prev.val, self.curr.next.val)
        copy = self.head.next
        while copy and copy.next:
            print("link list get after", copy.val, copy.prev.val, copy.next.val)
            copy = copy.next
        return res

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.curr.next = ListNode((key, value), self.curr)
        self.curr = self.curr.next
        self.curr.next = ListNode(0, self.curr) # add dummy node to end
        copy = self.head
        while copy:
            print("link list put", copy.val)
            copy = copy.next
        if key in self.memo:
            keyNode = self.memo[key]
            pre, after = keyNode.prev, keyNode.next
            pre.next, after.prev = after, pre
        elif self.cnt == self.capacity:
            print("over cap", key)
            copy = self.head
            while copy:
                print("link list put", copy.val)
                copy = copy.next
            print(self.memo, self.head.next.val)
            del self.memo[self.head.next.val[0]] # remove key from memo
            print(self.memo)
            delNode = self.head.next
            pre, after = delNode.prev, delNode.next
            pre.next, after.prev = after, pre
            #self.head.next, self.head.next.next.prev = self.head.next.next, self.head # skip the oldest node
            print(0)
            copy = self.head.next
            while copy and copy.next:
                print("link list put after", copy.val, copy.prev.val, copy.next.val)
                copy = copy.next
        else:
            print("counted!", key)
            self.cnt += 1

        self.memo[key] = self.curr # record {key: node in memo}
        copy = self.head

# Your LRUCache object will be instantiated and called as such:
if __name__ == '__main__':
     obj = LRUCache(1)
     obj.put(2,1)
     param_1 = obj.get(2)
     print(param_1)
     obj.put(3,2)
     param_1 = obj.get(2)
     print(param_1)
     param_1 = obj.get(3)
     print(param_1)
     obj.put(5,1)
     obj.put(3,2)
     obj.put(6,1)

