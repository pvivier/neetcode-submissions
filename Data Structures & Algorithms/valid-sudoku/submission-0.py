class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #list_of_lists_rows = = [[] for i in range(9)]
        list_of_columns = [[] for i in range(9)]
        list_of_squares = [[] for i in range(9)]
        for i,row in enumerate(board):
            for j,number in enumerate(row):
                if number != '.':
                    list_of_squares[j//3 + 3 * (i//3)].append(number)
                    list_of_columns[j].append(number)
        
        def check_duplicates(lis):
            for l in lis:
                if len(l) != len(set(l)):
                    print(l)
                    return False
            return True

        if not check_duplicates(list_of_columns):
            return False
        if not check_duplicates(list_of_squares):
            return False
        for l in board:
            l = [i for i in l if i != '.']
            if len(l) != len(set(l)):
                return False
        return True




