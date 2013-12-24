from Tree_test import Tree_test
from queue import PriorityQueue

class Haffman(Tree_test):
	'''khodet ye niga bendaz bebin in tree maker ro mitooni doros koni ya na'''
    
	def __init__(self,MyFile):
		Tree_test.__init__(self)
		self.File = str(open(MyFile, 'r').read())
		self.Data = {}
		self.dataQueue = PriorityQueue()
		self.tree = {}
        
	
	def repeatFinder(self):
		''' in tabe kheili rahate niazi be tozih nadare'''
		for i in self.File:
			if i in self.Data :
				self.Data[i] = self.Data[i] + 1
			else : 
				self.Data[i] = 1
		
		for i in self.Data.keys():
			self.dataQueue.put((self.Data[i], i))
		
	def treeMaker(self):
		'''in tabe derakhte hafman roo ba komake tavabe class haye digar doros mikone'''
		
		code_segment = '' # felan ziad mohem nis male oon paeine ke comment shode
		
		while not self.dataQueue.empty() :
			temp1, temp2 = self.dataQueue.get(), self.dataQueue.get() #kharej kardan do onsor az safe olaviat
			print(temp1,temp2) #baraye moshahedeye ettefaghat
			self.nodeJoin(temp1,temp2) #in tabe vasl konnandeye NODE ha be ham hast ke too Tree_test tarif shode
			if not self.dataQueue.empty() :
				self.dataQueue.put(self.currentNode) #vared kardan node jadide ijad shode be safe olaviat
			# ta in khat bayad derakht ma doros beshe hala dorosto ghalatesho khodet ye niga benadaz	
		
		
		#in tikeye paeinam ke asan velesh kon bayad dobare neveshte she.
		'''for i in range(len(self.objects)): #az inja be bad cherte val kon
			self.tree[self.objects[i].getLeftChild().getValue()[1]] = code_segment + '0'
			self.tree[self.objects[i].getRightChild().getValue()[1]] = code_segment + '1'
			if i%2 == 0 :
				code_segment = code_segment + '1'
			else :
				code_segment = code_segment + '0'
		'''		
	

					
a = Haffman("MyFile.txt")
a.repeatFinder()
print(a.Data)
a.treeMaker()

#print (a.tree)
   
