# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 00:22:36 2022

@author: 黄一一
"""

#%%
'''Brute-Force Version
   Time: O(n^2)
   Memory:O(1)'''

def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False


#%% Using hashset
'''Time:O(n)
    Memory:O(1)'''

def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hashset=set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
   
