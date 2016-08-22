import pdb
# This function takes board as an input
# returns three lists as described in README file
# In board, following convention is followed
#         1 -> musketeer
#         2 -> soldier
#         0 -> empty location
#         3 -> Soldier With Diamond (Goal State)
global WHITE,GRAY,BLACK;
WHITE = 0;
GRAY = 1
BLACK = 2
def checkColorWhite(matrix, location):
  if(matrix[location[0]][location[1]] == WHITE):
    return True;
  else:
    return False;
# def dfsVisit(board, loc, exploredNodes, searchQueue, shortestPath, colorMat, parent):
#   if(colorMat[loc[0]][loc[1]] == WHITE):
#     colorMat[loc[0]][loc[1]] = GRAY;
#     x = loc[0];
#     y = loc[1];
#     if(y-1 >= 0 and checkColorWhite(colorMat, [x,y-1]) == True):
#       dfsVisit(board, [x,y-1], exploredNodes, searchQueue, shortestPath, colorMat, parent);
#     if(x+1 < len(board) and checkColorWhite(colorMat, [x+1, y]) == True):
#       dfsVisit(board, [x+1, y], exploredNodes, searchQueue, shortestPath, colorMat, parent);
#     if(y+1 < len(board[x]) and checkColorWhite(colorMat, [x, y+1]) == True):
#       dfsVisit(board, [x, y+1], exploredNodes, searchQueue, shortestPath, colorMat, parent);
#     if(x-1 >= 0 and checkColorWhite(colorMat, [x-1, y]) == True):
#       dfsVisit(board, [x-1, y], exploredNodes, searchQueue, shortestPath, colorMat, parent);
def getLocOfMusketeers(board):
#every entry of a board is a list which represents the horizontal 
#configuration.
  size = len(board);
  i = 0;
  j = 0;
  temp = []
  for i in range(size):
    for j in range(len(board[i])):
      if(board[i][j] == 1):
        temp.append([i,j])
  return temp
def DFS(board, loc, exploredNodes, searchQueue, shortestPath):
  parent = [[[-1,-1] for i in range(len(board[0]))] for j in range(len(board))];
  colorMat = [[WHITE for i in range(len(board[0]))] for j in range(len(board))];
  iteration = 0;
  flag = 0;
  searchQueue.append([]);
  searchQueue[0].append([loc[0],loc[1]]);
  while(len(searchQueue[iteration]) != 0):
    x = searchQueue[iteration][0][0];
    y = searchQueue[iteration][0][1];
    exploredNodes.append([x,y]);
    colorMat[loc[0]][loc[1]] = GRAY;

    searchQueue.append(searchQueue[iteration][1:]);
    if(board[x][y] == 3):
      flag = 1;
      break;
    iteration+=1;
    # board[x-1][y] is for a soldier
    if(y-1 >= 0 and (board[x][y-1] == 2 or board[x][y-1] == 3) and checkColorWhite(colorMat, [x,y-1]) == True):
      colorMat[x][y-1] = GRAY;
      searchQueue[iteration].append([x, y-1]);
      parent[x][y-1] = [x,y];
    if(x+1 < len(board) and (board[x+1][y] == 2 or board[x][y-1] == 3) and checkColorWhite(colorMat, [x+1, y]) == True):
      colorMat[x+1][y] = GRAY;
      searchQueue[iteration].append([x+1, y]);
      parent[x+1][y] = [x,y];
    if(y+1 < len(board[x]) and (board[x][y+1] == 2 or board[x][y+1] == 3) and checkColorWhite(colorMat, [x,y+1]) == True):
      colorMat[x][y+1] = GRAY;
      searchQueue[iteration].append([x, y+1]);
      parent[x][y+1] = [x,y];
    if(x-1 >= 0 and (board[x-1][y] == 2 or board[x-1][y] == 3) and checkColorWhite(colorMat, [x-1,y]) == True):
      colorMat[x-1][y] = GRAY;
      searchQueue[iteration].append([x-1, y]);
      parent[x-1][y] = [x,y];    
    colorMat[loc[0]][loc[1]] = BLACK;
  if(flag == 1 and parent[x][y] != [-1,-1]):
    while(parent[x][y] != [-1,-1]):
      shortestPath.append([x,y]);
      [x,y] = parent[x][y];
    shortestPath.append([x,y]);
    shortestPath.reverse();
  del searchQueue[0]; 
def singleAgentSearch(board):
  exploredNodes = []
  searchQueue  = []
  shortestPath = []
  loc = getLocOfMusketeers(board);
  minExploredNodes =  [];
  minSearchQueue = [];
  minShortestPath =  [];
  minLength = 1000**1000;
  for i in range(len(loc)):
    exploredNodes = [];
    searchQueue = [];
    shortestPath = [];
    DFS(board, loc[i], exploredNodes, searchQueue, shortestPath);
    if(len(shortestPath) != 0 and len(shortestPath) < minLength):
      minLength = len(shortestPath);
      minExploredNodes = exploredNodes[:];
      minShortestPath = shortestPath[:];
      minSearchQueue = searchQueue[:];
  return (minExploredNodes, minSearchQueue, minShortestPath);