
"""
#	Constrcut a special pipeline class for Huoshu Tech. Inc. 
"""
from preprocessing import Preprocessing

class PipeLine(Preprocessing):
	"""docstring for PipeLine"""
	def __init__(self, config, df=None, filepath=None):
		super(PipeLine, self).__init__(config, df=df, filepath=filepath)

	# integrate some steps into a process
	def make_pipeline(self):
		self.read(). \
		update_config(). \
		cleaning(). \
		update_config_cols_indices(). \
		onehot_text(). \
		scaler(). \
		replacing(). \
		split() 
'''
	def print_info(self, text):	
		print('\n {} : \n'.format(text))
		print('text_cols_indices : \n ', self.config.text_cols_indices)
		print('number_cols_indices : \n ', self.config.number_cols_indices)
		print('data : \n ', self.data.describe())
		print('columns : ', self.columns)
		print('shape : ', self.data.shape)
'''

