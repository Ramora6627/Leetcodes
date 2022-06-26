class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = set()
        for digit in nums1:
            if digit in nums2:
                inter.add(digit)
                nums2.remove(digit)
        return list(inter)