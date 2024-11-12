def num_grid(lst):
    ans_lst = []
    for i in range(5):
       row_lst = []
       for j in range(5):
          mine_catch = 0
          if lst[i][j] == "#": row_lst.append("#")
          else:
            if i == 0 and j == 0:
                if lst[i+1][j] == "#": mine_catch += 1
                if lst[i][j+1] == "#": mine_catch += 1
                if lst[i+1][j+1] == "#": mine_catch += 1
                row_lst.append(str(mine_catch))
            elif i == 0 and j == 4:
                if lst[i+1][j] == "#": mine_catch += 1
                if lst[i][j-1] == "#": mine_catch += 1
                if lst[i+1][j-1] == "#": mine_catch += 1
                row_lst.append(str(mine_catch))
            elif i == 4 and j == 0:
                if lst[i-1][j] == "#": mine_catch += 1
                if lst[i][j+1] == "#": mine_catch += 1
                if lst[i-1][j+1] == "#": mine_catch += 1
                row_lst.append(str(mine_catch))
            elif i == 4 and j == 4:
                if lst[i-1][j] == "#": mine_catch += 1
                if lst[i][j-1] == "#": mine_catch += 1
                if lst[i-1][j-1] == "#": mine_catch += 1
                row_lst.append(str(mine_catch))
            elif i == 0 and (j != 0 or j!=4):
                if lst[i][j-1] == "#": mine_catch += 1
                if lst[i][j+1] == "#": mine_catch += 1
                if lst[i+1][j-1] == "#": mine_catch += 1
                if lst[i+1][j] == "#": mine_catch += 1
                if lst[i+1][j+1] == "#": mine_catch += 1
                row_lst.append(str(mine_catch))
            elif i == 4 and (j != 0 or j!=4):
                if lst[i][j-1] == "#": mine_catch += 1
                if lst[i][j+1] == "#": mine_catch += 1
                if lst[i-1][j-1] == "#": mine_catch += 1
                if lst[i-1][j] == "#": mine_catch += 1
                if lst[i-1][j+1] == "#": mine_catch += 1
                row_lst.append(str(mine_catch))
            elif j == 0 and (i != 0 or i!=4):
                if lst[i-1][j] == "#": mine_catch += 1
                if lst[i+1][j] == "#": mine_catch += 1
                if lst[i-1][j+1] == "#": mine_catch += 1
                if lst[i][j+1] == "#": mine_catch += 1
                if lst[i+1][j+1] == "#": mine_catch += 1
                row_lst.append(str(mine_catch))
            elif j == 4 and (i != 0 or i!=4):
                if lst[i-1][j] == "#": mine_catch += 1
                if lst[i+1][j] == "#": mine_catch += 1
                if lst[i-1][j-1] == "#": mine_catch += 1
                if lst[i][j-1] == "#": mine_catch += 1
                if lst[i+1][j-1] == "#": mine_catch += 1
                row_lst.append(str(mine_catch))   
            else:
                if lst[i-1][j-1] == "#": mine_catch += 1
                if lst[i-1][j] == "#": mine_catch += 1
                if lst[i-1][j+1] == "#": mine_catch += 1
                if lst[i][j-1] == "#": mine_catch += 1
                if lst[i][j+1] == "#": mine_catch += 1
                if lst[i+1][j-1] == "#": mine_catch += 1
                if lst[i+1][j] == "#": mine_catch += 1
                if lst[i+1][j+1] == "#": mine_catch += 1
                row_lst.append(str(mine_catch))
       ans_lst.append(row_lst)
    return ans_lst

lst_input = []
print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")
for e in input_list:lst_input.append([i for i in e.split()])
print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")