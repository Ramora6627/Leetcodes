class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r /3, c /3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True
#         for row in board:
            
#             filtered = filter(lambda x: x != ".", row)
#             v = list(filtered)
#             # print(v)
#             b = set(v)
#             if len(v) != len(b):
#                 # print("D")
#                 # print(set(filtered),list(filtered))
#                 return False
#         for j in range(9):
#             col = [board[i][j] for i in range(9) if board[i][j] != "."]
#             # print(col)
            
#             if len(set(col)) != len(col):
#                 # print(set(list(filtered)),list(filtered))
#                 # print("G")
#                 return False
#         for i in range(9):
#             grid = [board[i][j-3:j] for j in range(3,10,3)]
#             grid_v = [[board[j][i],board[j+1][i],board[j+2][i]] for j in range(0,9,3)]
#             print(grid_v)
#             for gr in grid:
#                 gr = filter(lambda x: x != ".", gr)
#                 a = list(gr)
#                 if len(set(a)) != len(a):
#                     # print(set(filtered),list(filtered))
#                     # print("h")
#                     return False
        # for j in range(9):
        #     grid_v = [[board[i][j],board[i+1][j],board[i+2][j]] for i in range(0,9,3)]
        #     # print(grid_v)
        #     for gr_v in grid_v:
        #         gr_v = filter(lambda x: x != ".", gr_v)
        #         g = list(gr_v)
        #         # print(g)
        #         if len(set(g)) != len(g):
        #             # print("s")
        #             # print(set(filtered),list(filtered))
        #             return False
        return True