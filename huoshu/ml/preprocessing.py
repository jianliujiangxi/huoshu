
"""
#	 Preprocessing the origin data includes cleaning, replacing, scaler, and abstracting features.
#	 
#	 read -> split -> cleaning -> replacing -> scaler -> abstracting 	
"""

import numpy as np
import pandas as pd
import copy
from sklearn.preprocessing import MaxAbsScaler, MinMaxScaler, StandardScaler, RobustScaler, PolynomialFeatures
from sklearn.decomposition import PCA, SparsePCA
from dataflow import DataFlow
import sys


class Preprocessing(object):
	"""docstring for Preprocessing"""
	def __init__(self, config, filepath=None, df=None):
		super(Preprocessing, self).__init__()
		self.config = config
		self.filepath = filepath
		self.dataframe = df

	def update_config(self):	
		self.config.text_cols_indices = list(range(4))	# the indices of text columns
		self.config.number_cols_indices = list(range(4,self.columns.shape[0]-1))	# the indices of numerical columns
		self.config.label = 'label'	# true label in actual data

		return self

	# read data	
	def read(self, show_head=False):
		if self.filepath != None:
			if self.filepath.split('.')[1] == 'csv':
				self.data = pd.read_csv(self.filepath)
			elif self.filepath.split('.')[1] in ['xlsx','xls']:
				self.data = pd.read_csv(self.filepath)
			else:	
				raise ValueError("The format of data filepath must be csv, xlsx, xls, and don't contain '.' in filename")
		else:		
			self.data = self.dataframe

		self.columns = self.data.columns	

		return self

	# cleaning data
	def cleaning(self):
		num_samples = self.data.shape[0]
		num_features = self.data.shape[1]
		self.old_columns = self.columns
		index = self.data.index

		# drop columns whose sum of Null is more than the ratio of num_samples except "label" column
		drop_columns = []
		for column in self.columns[:-1]:
			if self.data[column].isnull().sum() >= num_samples*self.config.drop_null_ratio:
				drop_columns.append(column)
		self.data = self.data.drop(drop_columns, axis=1)

		# drop rows whose sum of Null is more than the ratio of num_features
		inds = []
		for ind in index:
			if self.data.loc[ind].isnull().sum() >= num_features*self.config.drop_null_ratio or self.data[self.config.label][ind] == np.nan:
				inds.append(ind)
		self.data = self.data.drop(inds, axis=0)
		self.columns = self.data.columns
		return self

	# update the columns indices of text, number, and label in config	
	def update_config_cols_indices(self):	
		new_text_cols_indices = []
		new_number_cols_indices = []
		for ind, col in enumerate(self.columns): 
			if col in self.old_columns[self.config.text_cols_indices]:
				new_text_cols_indices.append(ind)
			elif col in self.old_columns[self.config.number_cols_indices]:	
				new_number_cols_indices.append(ind)
		self.config.text_cols_indices = new_text_cols_indices		
		self.config.number_cols_indices = new_number_cols_indices
		self.columns = self.data.columns

		return self


	# replacing data 
	def replacing(self, split=False):
		if split == False:
			for col in self.columns[:-1]:
				# print('col : ', col)
				# print('df mean : ', self.data[col].mean())
				if col in self.columns[self.config.text_cols_indices]:
					self.data[col] = self.data[col].fillna(-1)
					self.data[col] = self.data[col].replace([-np.inf, np.inf], -1)
				elif col in self.columns[self.config.number_cols_indices]:	
					self.data[col] = self.data[col].fillna(self.data[col].mean())
					self.data[col] = self.data[col].replace([-np.inf, np.inf], self.data[col].mean())
		else:
			pass
		return self	

	# one-hot text attributes
	def onehot_text(self):
		onehot_data = None
		for i, ind in enumerate(self.config.text_cols_indices):
			if i == 0:
				onehot_data = pd.get_dummies(self.data[self.columns[ind]])
			else:	
				onehot_col = pd.get_dummies(self.data[self.columns[ind]])
				onehot_data = pd.concat([onehot_data, onehot_col], axis=1)
		self.data = pd.concat([self.data[self.columns[:-1]], onehot_data, self.data[self.config.label]], axis=1)
		self.columns = self.data.columns
		return self


	# abstracting features
	def features_abstracting(self):
		method_dict = {'PCA':PCA(), 'SPCA':SparsePCA(n_components=self.config.spca_params['n_components'])}
		try:
			model = method_dict[self.config.method_fs]
		except:	
			raise ValueError("feature abstracting method {} don't exists".format(method))

		self.df.X_train = model.fit_transform(self.df.X_train.values)	
		self.df.X_test = model.transform(self.df.X_test)
		if self.config.validation:	
			self.df.X_valid = model.transform(self.df.X_valid)
			self.df.y_valid = self.df.y_valid.values
		
		self.df.y_train = self.df.y_train.values
		self.df.y_test = self.df.y_test.values

		return self

	# call DataFlow	
	def split(self):
		self.df = DataFlow(self.data, self.config).separate()

		return self

	# # cross the text features	
	# def features_cross(self):
	# 	pf = PolynomialFeatures(degree=len(self.config.text_cols_indices))
	# 	text_cols_indices_onehot = list(range(self.config.number_cols_indices[-1], self.columns.shape[0]-1))
	# 	text_cols = self.data[self.columns[text_cols_indices_onehot]]
	# 	text_cols_values = pf.fit_transform(text_cols.values)
	# 	text_cols = pd.DataFrame(text_cols_values, columns=text_cols.columns)
	# 	pass

	# scaler	
	def scaler(self):
		method = self.config.method_scaler
		try:
			if method == 'maxabs':
				ss = MaxAbsScaler()	
			elif method == 'minmax':
				ss = MinMaxScaler()	
			elif method == 'robust':
				ss = RobustScaler()	
			else:
				ss = StandardScaler()
		except:
			print('ERROR: There is no such method of ', method)

		numerical_cols = self.data[self.columns[self.config.number_cols_indices]]
		numerical_cols_values = ss.fit_transform(numerical_cols.values)	
		numerical_cols = pd.DataFrame(numerical_cols_values, columns=numerical_cols.columns)	

		temp_data = pd.concat([self.data[self.columns[self.config.number_cols_indices[-1]+1:-1]], numerical_cols], axis=1)
		self.data = pd.concat([temp_data, self.data['label']], join='inner', axis=1)	
		self.columns = self.data.columns
		self.config.text_cols_indices = list(range(self.columns.shape[0]-1-numerical_cols_values.shape[1]))
		self.config.number_cols_indices = list(range(self.config.text_cols_indices[-1]+1, self.columns.shape[0]))

		return self

