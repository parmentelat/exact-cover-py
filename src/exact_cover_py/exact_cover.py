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


@dataclass
class Matrix:
    """
    the sparse matrix that models a problem instance
    """
    root: Node

    # def debug(self):
    #     """
    #     roughly output the matrix
    #     """
    #     nav = self.root.right
    #     col_index = 0
    #     while nav is not self.root:
    #         print(f"===== column {col_index} has rows")
    #         row_nav = nav.down
    #         while row_nav is not nav:
    #             if row_nav is None:
    #                 print("XX", end=' ')
    #             else:
    #                 print(repr(row_nav), end=' ')
    #             row_nav = row_nav.down
    #         print()
    #         nav = nav.right
    #         col_index += 1


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