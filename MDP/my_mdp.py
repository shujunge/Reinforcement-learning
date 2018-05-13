import random as ran


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


if __name__ == "__main__":
	v = [0.0 for _ in range(0, 12)]
	md = mdp()
	num = 200000
	for k in range(1, num):
		for i in range(2, 10):
			s = i
			md.terminal = False
			md.gramm = 1
			value = 0
			while False == md.terminal:
				a = md.a[int(ran.random() * 4)]
				md.terminal, s, reward = md.return_value(s, a)
				value += md.gramm * reward
				md.gramm *= 0.5
			v[i] = (v[i] * (k - 1) + value) / k
		if k % 1000 == 0:
			print v
	print v


