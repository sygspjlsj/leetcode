class Solution(Object):
    def process(self, l1, l2):
        p1 = l1
        p2 = l2
        nums1 = 0
        nums2 = 0
        base = 1
        while p1 != None or p2 != None:
            if p1 != None:
                nums1 += p1.val * base
                p1 = p1.next
            if p2 != None:
                nums2 += p2.val * base
                p2 = p2.next
            base *= 10
        total = nums1 + nums2
        base = 10
        head = p = None
        while total > 0:
            tmp = ListNode(total % base)
            if head == None:
                head = tmp
                p = head
            else:
                p.next = tmp
                p = tmp
            total = total // base
        if p == None:
            head = ListNode(total % base)
        return head
