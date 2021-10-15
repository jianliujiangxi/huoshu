
"""
Configure setting with machine learning model
"""

class Configure(object):
	"""docstring for Configure"""
	def __init__(self):
		# paths
		self.save_model_path = '../results/models/'  # the path of saving ml models
		self.save_metric_path = '../results/metrics/' # the path of saving the metrics of model verification

		#==================== preprocessing parameters =================#
		self.random_state = 1234 # fixed random_state for every algorithm
		self.random_seed = 1234
		self.drop_null_ratio = 0.3	# drop the columns whose na ratio is more than the value

		# the method of abstracting features and relative paramters
		self.method_fs = 'SPCA'
		self.spca_params = {'n_components':100}
		self.pca_params = {'n_components':10}

		# the method of scaling input data
		self.method_scaler = 'standard'

		# Is or not validating
		self.validation = False

		# the method of separating data
		self.method_separate = 'random'
		self.train_ratio = 0.7
		self.test_ratio = 0.3
		if self.validation:
			self.train_ratio = 0.6
			self.test_ratio = 0.2
			self.valid_ratio = 0.2

	# reset configure when change some parameters		
	def reset(self):		
		pass


