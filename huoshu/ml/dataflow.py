
"""
	DEFINE a flow format for data to pass through any process
"""

from sklearn.model_selection import train_test_split
import random

class DataFlow(object):
	"""docstring for DataFlow"""
	def __init__(self, data, config):
		super(DataFlow, self).__init__()
		self.data = data 
		self.config = config

	def separate(self):
		method = self.config.method_separate
		validation = self.config.validation
		self.y = self.data[self.config.label]
		self.X = self.data.drop(self.config.label, axis=1)

		if method == 'rule':
			self.X_train, \
			self.X_test, \
			self.y_train, \
			self.y_test = call_rule(self.X, self.y)
		else:	
			lenth = list(range(self.data.shape[0]))

			if validation:
				assert self.config.train_ratio + self.config.valid_ratio + self.config.test_ratio == 1

				self.train_indices = random.sample(lenth, int(len(lenth)*self.config.train_ratio))
				for val in self.train_indices:
					lenth.remove(val)
				self.valid_indices = random.sample(lenth, int(len(lenth)*self.config.valid_ratio))
				for val in self.valid_indices:
					lenth.remove(val)
				self.test_indices = lenth

				self.X_train, \
				self.X_valid, \
				self.X_test, \
				self.y_train, \
				self.y_valid, \
				self.y_test = self.X.iloc[self.train_indices], \
								self.X.iloc[self.valid_indices], \
								self.X.iloc[self.test_indices], \
								self.y.iloc[self.train_indices], \
								self.y.iloc[self.valid_indices], \
								self.y.iloc[self.test_indices]
			else:					
				assert self.config.train_ratio + self.config.test_ratio == 1

				self.train_indices = random.sample(lenth, int(len(lenth)*self.config.train_ratio))
				for val in self.train_indices:
					lenth.remove(val)
				self.test_indices = lenth

				self.X_train, \
				self.X_test, \
				self.y_train, \
				self.y_test = self.X.iloc[self.train_indices], \
								self.X.iloc[self.test_indices], \
								self.y.iloc[self.train_indices], \
								self.y.iloc[self.test_indices]
		return self

	# cutormerize the rule of splitting data 
	def call_rule(self):
		pass	
