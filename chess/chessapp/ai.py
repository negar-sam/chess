class AI :
	

	
	
	def __init__(self, state="rnbqkbnr/pppppppp/......../......../......../......../PPPPPPPP/RNBQKBNR//"):
		self.state=state
		self.matrix=[list(self.convert_str(state)[i]) for i in range(8)]
		self.dead=[list(self.convert_str(state)[-2]),list(self.convert_str(state)[-1])]
	

	def __str__(self):
		return self.convert_matrix()

	def convert_str(self,  state):
		return state.split("/")	
	
	
	def convert_matrix(self):
		s=""
		for i in range(8):
			s=s+''.join(self.matrix[i])+"/"
		s=s+''.join(self.dead[0])+"/"+''.join(self.dead[1])
		return s
	
	
	def move_to_tuple(self, move):
		l=["A","B","C","D","E","F","G","H"]
		li={x:y for (x,y) in zip(l,range(8))}
		list1=(8-int(move[1]),li[move[0]],8-int(move[4]),li[move[3]])	
		return list1

	def list_of_possible_moves(self):
		state=self.state
		l=[]
		for i  in range(8):
			for j in range(8):
				pty=self.matrix[i][j]
				if pty=="R":
					directions=[[0,1],[1,0],[0,-1],[-1,0]]
					
					for m in range(4):
						newi=i
						newj=j
						while (0<= newi+directions[m][0] <8 and  0<=newj+directions[m][1] <8) :
							if self.matrix[newi+directions[m][0]][newj+directions[m][1]]=="." :
									l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
									newi=newi+directions[m][0]
									newj=newj+directions[m][1]
							elif  "a"<=self.matrix[newi+directions[m][0]][newj+directions[m][1]]<="z":
								l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
								break
							else:
								break
				if pty=="B" :
					directions=[[1,1],[1,-1],[-1,1],[-1,-1]]
					for m in range(4):
						newi=i
						newj=j
						while(0<= newi+directions[m][0] <8 and  0<=newj+directions[m][1] <8) :
							if self.matrix[newi+directions[m][0]][newj+directions[m][1]]=="." :
								l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
								newi=newi+directions[m][0]
								newj=newj+directions[m][1]
							elif  "a"<=self.matrix[newi+directions[m][0]][newj+directions[m][1]]<="z":
								l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
								break
							else:
								break
				if pty=="Q" :
					directions=[[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[1,0],[0,-1],[-1,0]]
					for m in range(8):
						newi=i
						newj=j
						while(0<= newi+directions[m][0] <8 and  0<=newj+directions[m][1] <8) :	
							if self.matrix[newi+directions[m][0]][newj+directions[m][1]]=="." :
								l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
								newi=newi+directions[m][0]
								newj=newj+directions[m][1]
							elif  "a"<=self.matrix[newi+directions[m][0]][newj+directions[m][1]]<="z":
								l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
								break
							else:
								break
				if pty=="P":
					if 0<=i-1<8 and self.matrix[i-1][j]=="." :
						l.append([i,j,i-1,j])
					if  i==6 and self.matrix[i-2][j]=="." and self.matrix[i-1][j]==".":
						l.append([i,j,i-2,j])
					if 0<=i-1<8 and 0<=j+1<8 and "a"<=self.matrix[i-1][j+1]<="z":
						l.append([i,j,i-1,j+1])
					if 0<=i-1<8 and 0<=j-1<8 and "a"<=self.matrix[i-1][j-1]<="z":
						l.append([i,j,i-1,j-1])

				if pty=="K":
					directions=[[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
					for m in range(8):
						if 0<= i+directions[m][0] <8 and  0<=j+directions[m][1] <8 :
							if not "A"<=self.matrix[i+directions[m][0]][j+directions[m][1]]<="Z":
								l.append([i,j,i+directions[m][0] , j+directions[m][1]])
				if  pty=="N":
					directions=[[1,2],[-1,2],[2,1],[2,-1],[-2,1],[-2,-1],[1,-2],[-1,-2]]
					for m in range(8):
						if 0<= i+directions[m][0] <8 and  0<=j+directions[m][1] <8 :
							if not "A"<=self.matrix[i+directions[m][0]][j+directions[m][1]]<="Z":
				 				l.append([i,j,i+directions[m][0] , j+directions[m][1]])						
		l = [tuple(x) for x in l]
		return l

	def check_correct_move(self, move):
		mv=self.move_to_tuple(move)
		li=self.user_final_moves()
		pty=self.matrix[mv[0]][mv[1]]
		if mv in li:
			if "a"<=self.matrix[mv[2]][mv[3]]<="z":
				self.dead[1].append(self.matrix[mv[2]][mv[3]])
			self.matrix[mv[0]][mv[1]]="."
			self.matrix[mv[2]][mv[3]]=pty
			return True
		else:
			return False
	def user_status_change(self, mv):
		pty=self.matrix[mv[0]][mv[1]]
		if "a"<=self.matrix[mv[2]][mv[3]]<="z":
			self.dead[1].append(self.matrix[mv[2]][mv[3]])
		self.matrix[mv[0]][mv[1]]="."
		self.matrix[mv[2]][mv[3]]=pty
	

	def list_of_possible_moves_of_ai(self):
		state=self.state
		l=[]
		for i  in range(8):
			for j in range(8):
				pty=self.matrix[i][j]
				if pty=="r":
					directions=[[0,1],[1,0],[0,-1],[-1,0]]
					
					for m in range(4):
						newi=i
						newj=j
						while (0<= newi+directions[m][0] <8 and  0<=newj+directions[m][1] <8) :
							if self.matrix[newi+directions[m][0]][newj+directions[m][1]]=="." :
									l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
									newi=newi+directions[m][0]
									newj=newj+directions[m][1]
							elif  "A"<=self.matrix[newi+directions[m][0]][newj+directions[m][1]]<="Z":
								l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
								break
							else:
								break
				if pty=="b" :
					directions=[[1,1],[1,-1],[-1,1],[-1,-1]]
					for m in range(4):
						newi=i
						newj=j
						while(0<= newi+directions[m][0] <8 and  0<=newj+directions[m][1] <8) :
							if self.matrix[newi+directions[m][0]][newj+directions[m][1]]=="." :
								l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
								newi=newi+directions[m][0]
								newj=newj+directions[m][1]
							elif  "A"<=self.matrix[newi+directions[m][0]][newj+directions[m][1]]<="Z":
								l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
								break
							else:
								break
				if pty=="q" :
					directions=[[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[1,0],[0,-1],[-1,0]]
					for m in range(8):
						newi=i
						newj=j
						while(0<= newi+directions[m][0] <8 and  0<=newj+directions[m][1] <8) :	
							if self.matrix[newi+directions[m][0]][newj+directions[m][1]]=="." :
								l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
								newi=newi+directions[m][0]
								newj=newj+directions[m][1]
							elif  "A"<=self.matrix[newi+directions[m][0]][newj+directions[m][1]]<="Z":
								l.append([i, j, newi+directions[m][0] ,  newj+directions[m][1]])
								break
							else:
								break
				if pty=="p":
					if 0<=i+1<8 and self.matrix[i+1][j]=="." :
						l.append([i,j,i+1,j])
					if  i==1 and self.matrix[i+2][j]=="." and self.matrix[i+1][j]==".":
						l.append([i,j,i+2,j])
					if 0<=i+1<8 and 0<=j+1<8 and "A"<=self.matrix[i+1][j+1]<="Z":
						l.append([i,j,i+1,j+1])
					if 0<=i+1<8 and 0<=j-1<8 and "A"<=self.matrix[i+1][j-1]<="Z":
						l.append([i,j,i+1,j-1])

				if pty=="k":
					directions=[[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
					for m in range(8):
						if 0<= i+directions[m][0] <8 and  0<=j+directions[m][1] <8 :
							if not "a"<=self.matrix[i+directions[m][0]][j+directions[m][1]]<="z":
								l.append([i,j,i+directions[m][0] , j+directions[m][1]])
				if  pty=="n":
					directions=[[1,2],[-1,2],[2,1],[2,-1],[-2,1],[-2,-1],[1,-2],[-1,-2]]
					for m in range(8):
						if 0<= i+directions[m][0] <8 and  0<=j+directions[m][1] <8 :
							if not "a"<=self.matrix[i+directions[m][0]][j+directions[m][1]]<="z":
				 				l.append([i,j,i+directions[m][0] , j+directions[m][1]])						
		l = [tuple(x) for x in l]
		return l

	def heuristic_value(self):
		hdic={"p":1,"n":3,"b":3,"r":5,"q":9,"k":-1000,".":0,"P":-1,"N":-3,"B":-3,"R":-5,"Q":-9,"K":1000}
		value=0
		for i in range(8):
			for j in range(8):
				value=value+hdic[self.matrix[i][j]]
		return value
	def change_status(self,move):
		if "A"<=self.matrix[move[2]][move[3]]<="Z":
			self.dead[0].append(self.matrix[move[2]][move[3]])
		self.matrix[move[2]][move[3]]=self.matrix[move[0]][move[1]]
		self.matrix[move[0]][move[1]]="."
	def alphabeta(self,depth,alpha,beta,maximizingplayer):
		if depth==0 :
			return (self.heuristic_value(), None)
		if maximizingplayer :
			v=(-10000,None)
			if(depth == 4):
				li_moves = self.ai_final_moves()
			else:
				li_moves = self.list_of_possible_moves_of_ai()
			for i in li_moves:
				tmp = AI(self.convert_matrix())
				tmp.change_status(i)
				ans=tmp.alphabeta(depth-1,alpha,beta,False)
				if ans[0]>v[0]:
					v=(ans[0],i)
				alpha=max(alpha,v[0])
				if beta <= alpha :
					break
			return v
		else:
			v=(10000,None)
			for i in self.list_of_possible_moves():
				tmp=AI(self.convert_matrix())
				tmp.user_status_change(i)					
				ans=tmp.alphabeta(depth-1,alpha,beta,True)
				if ans[0]<v[0]:
					v=(ans[0],i)
				beta=min(beta,v[0])
				if beta <= alpha:
					break
			return v			
	def ai_king_in_danger(self):
		li=self.list_of_possible_moves()
		for mv in li:
			if self.matrix[mv[2]][mv[3]]=="k":
				return True
		return False
	def user_king_in_danger(self):
		li=self.list_of_possible_moves_of_ai()
		for mv in li:
			if self.matrix[mv[2]][mv[3]]=="K":
				return True
		return False
	def ai_final_moves(self):
		li=self.list_of_possible_moves_of_ai()
		ans=[]
		for mv in li:
			state=AI(self.convert_matrix())
			state.change_status(mv)	
			if not state.ai_king_in_danger():
				ans.append(mv)
		return ans
	def user_final_moves(self):
		li=self.list_of_possible_moves()
		ans=[]
		for mv in li:
			state=AI(self.convert_matrix())
			state.change_status(mv)
			if not state.user_king_in_danger():
				ans.append(mv)
		return ans
if __name__ == "__main__":
	test = AI()
	move = input()
	test.check_correct_move(move)
	print(test)
	mv = test.alphabeta(3, -10000, +10000, 1)[1]
	test.change_status(mv)
	print(test)
	