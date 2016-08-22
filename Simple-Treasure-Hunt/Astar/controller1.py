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
def getLocation(board, value):
	temp = [];
	for i in range(len(board)):
		for j in range(len(board[i])):
			if(board[i][j] == value):
				temp.append([i,j]);
	return temp;
def parent(index):
	if(index != 0):
		return (index - 1)/2;
	else:
		return 0;
def rChild(index):
	return 2*index + 1;
def lChild(index):
	return 2*index + 2;
class Heap:
	currentSize = 0;
	heapList = [];
	def addNode(self, pair, hDistance, gDistance):
		# adds a node to the heap list
		self.heapList.append([pair, hDistance, gDistance]);
		self.currentSize+=1;
		index = self.currentSize-1;
		while(self.heapList[parent(index)][1] + self.heapList[parent(index)][2]> self.heapList[index][1] + self.heapList[index][2]):
			temp = self.heapList[parent(index)];
			self.heapList[parent(index)] = self.heapList[index];
			self.heapList[index] = temp;
			index = parent(index);
	def minHeapify(self, index):
		minimum = index;
		if(rChild(index) < self.currentSize and self.heapList[rChild(index)][1] + self.heapList[rChild(index)][2] < self.heapList[minimum][1] + self.heapList[minimum][2]):
			minimum = rChild(index);
		if(lChild(index) < self.currentSize and self.heapList[lChild(index)][1] + self.heapList[lChild(index)][2] < self.heapList[minimum][1] + self.heapList[minimum][2]):
			minimum = lChild(index);
		if(minimum != index):
			temp = self.heapList[index];
			self.heapList[index] = self.heapList[minimum];
			self.heapList[minimum] = temp;
			self.minHeapify(minimum);
	def buildHeap(self):
		for i in range(parent(self.currentSize-1),-1,-1):
			self.minHeapify(i);
	def extractMin(self):
		if(self.currentSize > 1):
			temp = self.heapList[0];
			self.heapList[0] = self.heapList[self.currentSize-1];
			del self.heapList[self.currentSize-1];
			self.currentSize-=1;
			self.minHeapify(0);
			return temp;
		elif(self.currentSize == 1):
			self.currentSize-=1;
			temp = self.heapList[0];
			self.heapList = [];
			return temp;
		else:
			print "Heap empty\n";
	def clearAll(self):
		currentSize = 0;
		self.heapList = [];
def heuristic(locDiamond, currentLoc):
	return (abs(locDiamond[0]-currentLoc[0]) + abs(locDiamond[1]-currentLoc[1]));
def getIndex(l, tup):
	# this function returns the index of tup in list l
	for i in range(len(l)):
		if(l[i] == tup):
			return i;
	else:
		return -1;
def aStarSearch(board, loc, exploredNodes, searchQueue, shortestPath):
	diamondLoc = getLocation(board, 3);
	if(len(diamondLoc) == 0):
		return ;
	diamondLoc = diamondLoc[0];
	parent = [[[-1,-1] for i in range(len(board[0]))] for j in range(len(board))];
	colorMat = [[WHITE for i in range(len(board[0]))] for j in range(len(board))];
	iteration = 0;
	searchQueue.append([]);
	searchQueue[0].append([loc[0],loc[1]]);
	h = Heap();
	h.clearAll();
	g = 0;
	flag = 0;
	h.addNode(loc, g, heuristic(loc, diamondLoc));
	while(h.currentSize > 0):
		[[x,y], gValue, hValue] = h.extractMin();
		exploredNodes.append([x,y]);
		searchQueue.append(searchQueue[iteration][:]);
		iteration+=1;		
		ind = getIndex(searchQueue[iteration], [x,y]);
		del searchQueue[iteration][ind];
		# board[x-1][y] is for a soldier
		if(board[x][y] == 3):
			flag = 1;
			break;
		if(y-1 >= 0 and (board[x][y-1] == 2 or board[x][y-1] == 3) and colorMat[x][y-1] == WHITE):
			colorMat[x][y-1] = GRAY;
			l = heuristic([x,y-1], diamondLoc);
			h.addNode([x,y-1], gValue + 1, l);
			searchQueue[iteration].append([x, y-1]);
			parent[x][y-1] = [x,y];
		if(x+1 < len(board) and (board[x+1][y] == 2 or board[x+1][y] == 3) and colorMat[x+1][y] == WHITE):
			colorMat[x+1][y] = GRAY;
			l = heuristic([x+1,y], diamondLoc)
			h.addNode([x+1,y], gValue + 1, l);			
			searchQueue[iteration].append([x+1, y]);
			parent[x+1][y] = [x,y];
		if(y+1 < len(board[x]) and (board[x][y+1] == 2 or board[x][y+1] == 3) and colorMat[x][y+1] == WHITE):
			colorMat[x][y+1] = GRAY;
			l = heuristic([x,y+1], diamondLoc);
			h.addNode([x,y+1], gValue + 1, l);						
			searchQueue[iteration].append([x, y+1]);
			parent[x][y+1] = [x,y];
		if(x-1 >= 0 and (board[x-1][y] == 2 or board[x-1][y] == 3) and colorMat[x-1][y] == WHITE):
			colorMat[x-1][y] = GRAY;
			l = heuristic([x-1,y], diamondLoc);
			h.addNode([x-1,y], gValue + 1, l);			
			searchQueue[iteration].append([x-1, y]);
			parent[x-1][y] = [x,y];
		colorMat[x][y] = BLACK;
	if(flag == 1 and parent[x][y] != [-1,-1]):
		while(parent[x][y] != [-1,-1]):
			shortestPath.append([x,y]);
			[x,y] = parent[x][y];
		shortestPath.append([x,y]);
		shortestPath.reverse();
	del searchQueue[0];		
def singleAgentSearch(board):
	loc = getLocation(board, 1); # of the musketeers
	minExploredNodes =  [];
	minSearchQueue = [];
 	minShortestPath =  [];
	minLength = 1000**1000;
	usedExpl = [];
	usedSearch = [];
	for i in range(len(loc)):
		exploredNodes = [];
		searchQueue = [];
		shortestPath = [];
		aStarSearch(board, loc[i], exploredNodes, searchQueue, shortestPath);
		if(len(shortestPath) != 0 and len(shortestPath) < minLength):
			minLength = len(shortestPath);
			minExploredNodes = exploredNodes[:];
			minShortestPath = shortestPath[:];
			minSearchQueue = searchQueue[:];
		elif(len(shortestPath) == 0):
			minExploredNodes = exploredNodes[:];
			minSearchQueue = searchQueue[:];
	return (minExploredNodes, minSearchQueue, minShortestPath);
	# YOUR CODE HERE #
# pdb.set_trace();
# board = [[0, 2, 2, 2, 1],
# 		[2, 2, 2, 0, 2],
# 		[2, 1, 0, 2, 2], 
# 		[0, 0, 0, 2, 2], 
# 		[3, 0, 2, 2, 0]];
# c = singleAgentSearch(board);
# print c