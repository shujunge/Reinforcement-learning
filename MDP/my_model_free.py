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
		
		self.gamma = 0.8


	def tranform(self, states, action):
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


##############   epsilon greedy policy #####
def epsilon_greedy(mdp,qfunc, state, epsilon):
	## max q action
	amax = 0
	key = "%d_%s" % (state, mdp.a[0])
	qmax = qfunc[key]
	for i in xrange(len(mdp.a)):
		key = "%d_%s" % (state, mdp.a[i])
		q = qfunc[key]
		if qmax < q:
			qmax = q
			amax = i
		
		##probability
	pro = [0.0 for i in xrange(len(mdp.a))]
	pro[amax] += 1 - epsilon
	for i in xrange(len(mdp.a)):
		pro[i] += epsilon / len(mdp.a)

	##choose
	r = ran.random()
	s = 0.0
	for i in xrange(len(mdp.a)):
		s += pro[i]
		if s >= r:
			return mdp.a[i]
	return mdp.a[len(mdp.a) - 1]

def qlearning(mdp,num_iter1, alpha,epsilon):
	qfunc=dict()
	for s in mdp.states:
		for a in mdp.a:
			key="%d_%s"%(s,a)
			qfunc[key]=0.0
			
	for iter in xrange(num_iter1):
		s=mdp.states[int(ran.random()*len(mdp.states))]
		a=mdp.a[int(ran.random()*len(mdp.a))]
		t=False
		cout=0
		while False==t and cout <100:
			key="%d_%s"%(s,a)
			t,s1,r=mdp.tranform(s,a)
			key1=""
			qmax=-1.0
			for a1 in mdp.a:
				if qmax<qfunc["%d_%s"%(s1,a1)]:
					qmax=qfunc["%d_%s"%(s1,a1)]
					key1="%d_%s"%(s1,a1)
					a=a1
			qfunc[key]=qfunc[key]+alpha*(r+mdp.gamma*qfunc[key1]-qfunc[key])
			s=s1
			a=epsilon_greedy(mdp,qfunc,s,epsilon)
			cout+=1
	return qfunc

def sarsa(mdp,num_iter1, alpha,epsilon):
	qfunc=dict()
	for s in mdp.states:
		for a in mdp.a:
			key="%d_%s"%(s,a)
			qfunc[key]=0.0
	for iter in xrange(num_iter1):
		s=mdp.states[int(ran.random()*len(mdp.states))]
		a=mdp.a[int(ran.random()*len(mdp.a))]
		t=False
		cout=0
		while False==t and cout <100:
			key="%d_%s"%(s,a)
			t,s1,r=mdp.tranform(s,a)
			a1=epsilon_greedy(mdp,qfunc,s,epsilon)
			key1="%d_%s"%(s1,a1)
			qfunc[key]=qfunc[key]+alpha*(r+mdp.gamma*qfunc[key1]-qfunc[key])
			s=s1
			a=a1#epsilon_greedy(mdp,qfunc,s,epsilon)
			cout+=1
	return qfunc

if __name__=="__main__":
	md=mdp()
	ss=qlearning(md,5000,0.2,0.2)
	print(ss)
	print(ss["5_d"])
	print(ss["7_d"])
	print(ss["9_d"])
	print(ss["3_u"])
	for i,v in ss.items():
		if v > 1e-04:
			print i,v

