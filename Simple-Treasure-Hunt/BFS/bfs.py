import pdb
def search(l, e):
	# l is the list from which the element e is to be searched
	# In case the element e is not in the list l, then -1 is returned
	# Otherwise the index of the element e in l is returned.
	for i in range(len(l)):
		for j in range(len(l[i])):
			if(l[i][j] == e):
				return 1;
	return -1;
def BFS(board, loc, exploredNodes, searchQueue, shortestPath):
	# searchQueue is a list of lists searchQueue after every 
	#iteration
	# searchQueue = [];
	# exploredNodes = [];
	# shortestPath = [];
	parent = [[(-1,-1) for i in range(len(board[0]))] for j in range(len(board))];
	iteration = 0;
	searchQueue.append([]);
	searchQueue[0].append((loc[0],loc[1]));
	while(len(searchQueue[iteration]) != 0):
		x = searchQueue[iteration][0][0];
		y = searchQueue[iteration][0][1];
		exploredNodes.append((x,y));
		searchQueue.append(searchQueue[iteration][1:]);
		iteration+=1;
		# board[x-1][y] is for a soldier
		if(board[x][y] == 3):
			break;
		if(y-1 >= 0 and (board[x][y-1] == 2 or board[x][y-1] == 3) and search(searchQueue, (x,y-1)) == -1):
			searchQueue[iteration].append((x, y-1));
			parent[x][y-1] = (x,y);
		if(x+1 < len(board) and (board[x+1][y] == 2 or board[x][y-1] == 3) and search(searchQueue, (x+1, y)) == -1):
			searchQueue[iteration].append((x+1, y));
			parent[x+1][y] = (x,y);
		if(y+1 < len(board[x]) and (board[x][y+1] == 2 or board[x][y+1] == 3) and search(searchQueue, (x,y+1)) == -1):
			searchQueue[iteration].append((x, y+1));
			parent[x][y+1] = (x,y);
		if(x-1 >= 0 and (board[x-1][y] == 2 or board[x-1][y] == 3) and search(searchQueue, (x-1, y)) == -1):
			searchQueue[iteration].append((x-1, y));
			parent[x-1][y] = (x,y);
	if(parent[x][y] != (-1,-1)):
		while(parent[x][y] != (-1,-1)):
			shortestPath.append((x,y));
			(x,y) = parent[x][y];
		shortestPath.append((x,y));
		shortestPath.reverse();
	del searchQueue[0];
board = [[2,2,0,0],
		 [0,1,2,2],
		 [0,2,3,2],
		 [2,0,2,0]];
loc = (1,1);
exploredNodes = [];
searchQueue = [];
shortestPath = [];
pdb.set_trace();
BFS(board, loc, exploredNodes, searchQueue, shortestPath);
print "Explored Nodes ",exploredNodes,'\n';
print "SearchQueue ",searchQueue,'\n';
print "Shortest Path ",shortestPath,'\n';