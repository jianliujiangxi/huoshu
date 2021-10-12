import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="huoshu",
	version="1.1.4",
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