class mdp():
	def __init__(self):
		self.a = ['u', 'd', 'l', 'r']
		self.states = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
		self.t = dict()
		self.t["2_r"] = 3
		self.t["2_d"] = 6
		self.t["3_u"] = 1
		self.t["3_l"] = 2
		self.t["3_r"] = 4
		self.t["3_d"] = 7
		self.t["4_l"] = 3
		self.t["4_d"] = 8
		self.t["5_r"] = 6
		self.t["5_d"] = 10
		self.t["6_l"] = 5
		self.t["6_r"] = 7
		self.t["6_u"] = 2
		self.t["7_d"] = 11
		self.t["7_u"] = 3
		self.t["7_l"] = 6
		self.t["7_r"] = 8
		self.t["8_u"] = 4
		self.t["8_l"] = 7
		self.t["8_r"] = 9
		self.t["9_d"] = 12
		self.t["9_l"] = 8
		
		self.r = dict()
		self.r["5_d"] = -1
		self.r["7_d"] = -1
		self.r["3_u"] = 1
		self.r["9_d"] = -1
		
		self.end = [1, 10, 11, 12]
		self.terminal = False
		
		self.gramm = 0.8
	
	def return_value(self, states, action):
		if states in self.end:
			self.terminal = True
		else:
			self.terminal = False
		
		key = "%d_%s" % (states, action)
		
		if key in self.t:
			next_states = self.t[key]
		else:
			next_states = states
		
		if key in self.r:
			reward = self.r[key]
		else:
			reward = 0
		return self.terminal, next_states, reward

class policy_value:
	def __init__(self,mdp):
		self.v=[0.0 for _ in range(len(mdp.states))]
		self.pi=dict()
		
		for states in mdp.states:
			if states in mdp.end:
				continue
			else:
				self.pi[states]=mdp.a[0]
		
	def value_iteration(self,mdp):
		for k in range(1,10000):
			delta=0.0
			for i in range(2,10):
				current_states=i
				a1=mdp.a[0]
				t,next_states,r=mdp.return_value(current_states,a1)
				v1=r+mdp.gramm*self.v[next_states]
				
				for act in mdp.a:
					action=act
					t, next_states, r = mdp.return_value(current_states, action)
					if v1<= r + mdp.gramm * self.v[next_states]:
						a1=action
						v1=r + mdp.gramm * self.v[next_states]
					
				delta+=abs(v1-self.v[i])
				self.v[i] = v1
				self.pi[i] = a1
				
			if delta<=1e-6:
				break
	
	
	def policy_evaluate(self,mdp):
		for _ in range(1000):
			delta=0.0
			for states in range(2,10):
				action=self.pi[states]
				t,next_state,r=mdp.return_value(states,action)
				v1=r+mdp.gramm*self.v[next_state]
				
				delta+=abs(self.v[states]-v1)
				self.v[states] = v1
			if delta<=1e-6:
				break

	def policy_improve(self,mdp):
		for states in range(2,10):
			a1=mdp.a[0]
			t, next_state, r = mdp.return_value(states, a1)
			v1 = r + mdp.gramm * self.v[next_state]
			for i in mdp.a:
				action=i
				t, next_state, r = mdp.return_value(states, action)
				if v1 < r + mdp.gramm * self.v[next_state]:
					a1=action
					v1=r + mdp.gramm * self.v[next_state]
				
			self.pi[states]=a1
		
	def policy_iteration(self,mdp):
		for _ in range(10000):
			self.policy_evaluate(mdp)
			self.policy_improve(mdp)
	
			
			
	
if __name__ == "__main__":

	md = mdp()
	pl=policy_value(md)
	pl.value_iteration(md)
	# pl.policy_iteration(md)
	print(pl.v)
	print(pl.pi)


