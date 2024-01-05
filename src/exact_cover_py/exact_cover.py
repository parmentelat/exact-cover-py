"""
Donald Knuth's Algorithm X implemented in Python.
"""

from dataclasses import dataclass

import numpy as np

@dataclass
class Node:
    """
    Node in a doubly-linked list.
    """
    left: 'Node'
    right: 'Node'
    up: 'Node'
    down: 'Node'
    # point to relative column header, also referred to as col_node
    # None for the col headers themseves
    col: 'Node'
    # row index for the non-header nodes
    # -1 for the header nodes
    row: int

    def __repr__(self):
        # a header node
        if self.col is None:
            return "header"
        else:
            return f"{self.row}x{self.col.row}"

    def insert_horizontally_after(self, where):
        """
        attach self to the right of where
        if where is None, self gets the single node in its row
        """
        if where is None:
            self.left = self
            self.right = self
        else:
            self.right = where.right
            self.left = where
            where.right.left = self
            where.right = self

    def insert_vertically_after(self, where):
        """
        attach self below where
        if where is None, self gets the single node in its column
        """
        if where is None:
            self.up = self
            self.down = self
        else:
            self.down = where.down
            self.up = where
            where.down.up = self
            where.down = self

    def cover_horizontally(self):
        """
        remove self from the row
        """
        if self.right is self:
            return
        self.right.left = self.left
        self.left.right = self.right

    def uncover_horizontally(self):
        """
        reinsert self into the row
        """
        self.right.left = self
        self.left.right = self

    def cover_vertically(self):
        """
        remove self from the column
        """
        if self.down is self:
            return
        self.down.up = self.up
        self.up.down = self.down

    def uncover_vertically(self):
        """
        reinsert self into the column
        """
        self.down.up = self
        self.up.down = self

    def cover_column(self):
        """
        remove the column from the matrix
        self is expected to be a column header
        """
        self.cover_horizontally()
        # iterating on the rows below the header
        nav_row = self.down
        while nav_row is not self:
            # iterating on the columns of the row
            nav_col = nav_row.right
            while nav_col is not nav_row:
                nav_col.cover_vertically()
                nav_col = nav_col.right
            nav_row = nav_row.down

    def uncover_column(self):
        """
        reinsert the column into the matrix
        self is expected to be a column header
        """
        # iterating on the rows above the header
        nav_row = self.up
        while nav_row is not self:
            # iterating on the columns of the row
            nav_col = nav_row.left
            while nav_col is not nav_row:
                nav_col.uncover_vertically()
                nav_col = nav_col.left
            nav_row = nav_row.up
        self.uncover_horizontally()

@dataclass
class Matrix:
    """
    the sparse matrix that models a problem instance
    """
    root: Node

    def reverse(self):
        """
        reconstruct the input matrix for debugging
        """
        nav_col = self.root.right
        ones = set()
        col_index = 0
        while nav_col is not self.root:
            nav_row = nav_col.down
            while nav_row is not nav_col:
                ones.add((nav_row.row, nav_row.col.row))
                nav_row = nav_row.down
            nav_col = nav_col.right
            col_index += 1

        rows, cols = (max(ones, key=lambda x: x[0])[0],
                      max(ones, key=lambda x: x[1])[1])

        loop = np.zeros((rows+1, cols+1), dtype=np.uint8)
        for row, col in ones:
            loop[row, col] = True
        return loop

    @staticmethod
    def from_numpy(array: np.ndarray) -> 'Matrix':
        """
        Create a matrix from a numpy array.
        """
        # create the colomn headers
        _, width = array.shape
        root = nav = Node(None, None, None, None, None, -1)
        root.right = root.left = root
        # for direct access to the column headers
        column_headers = []
        for col_index in range(width):
            col_node = Node(None, None, None, None, None, col_index)
            col_node.insert_horizontally_after(nav)
            col_node.down = col_node.up = col_node
            nav = col_node
            column_headers.append(col_node)
        nav.right = root
        # fill the matrix
        for row_index, row in enumerate(array):
            where_in_row = None
            for col_index, (col_node, value) in enumerate(
                zip(column_headers, row)):
                if value:
                    node = Node(None, None, None, None, col_node, row_index)
                    # connect horizontally
                    node.insert_horizontally_after(where_in_row)
                    where_in_row = node
                    # connect vertically
                    where_in_column = column_headers[col_index].up
                    node.insert_vertically_after(where_in_column)

        return Matrix(root)