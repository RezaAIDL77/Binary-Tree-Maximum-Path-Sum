#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:13:36 2020
124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
 node to any node in the tree along the parent-child connections. 
 The path must contain at least one node and does not need to go through the root.


@author: rezarashetnia
"""

class Solution:
    def maxPathSum(self,root):
        def maxroot(Node):
            if not Node:
                return 0
            leftval = max(maxroot(Node.left),0)
            rightval = max(maxroot(Node.right),0)
            withroot = Node.val+leftval+rightval
            self.maxval = max(self.maxval,withroot)
            return Node.val+max(leftval,rightval)
        
        self.maxval = float('-inf')
        maxroot(root)
        return self.maxval
