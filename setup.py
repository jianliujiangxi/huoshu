import setuptools

with open("README.md", "rb") as fh:
	long_description = fh.readlines()

setuptools.setup(
	name="huoshu",
	version="0.0.3",
	author="Jian Liu",
	author_email="jianliu9509@outlook.com",
	description="A small example package for HuoShu Tech. to compelete",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/pypa/sampleproject",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	install_requires=[
		'pandas',
		'psycopg2',
		'sqlalchemy'
	]
)