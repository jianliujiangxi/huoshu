
# The package is proposed to create some basic methods for saving time and human power of algorithm engineers of ***HuoShu Tech. Inc.***

 *Welcome every engineer of HuoShu to become the contributor in this big project!!!*

## Project Content
```bash
.
├─build
│  ├─bdist.win-amd64
│  └─lib
│      └─huoshu
├─dist
├─huoshu
│  └─__pycache__
└─huoshu.egg-info
```

There will be all source code implemented by Liu Jian in the directory named "**huoshu**"

## Install
```python
pip install huoshu
```

## Documents

- HuoShuSql.py -- provied some basic algorithm to operate and transform the data flow between pandas.DataFrame and PostgreSql, which include link the postgresql of HuoShu Tech. Inc., transform the data format between dataframe and sql, and write the data into sql database.  

The improvements of HuoShuSql to finish:
1. - [ ] add some other important basic operation such like "insert Table", "delete Table", and etc. 
2. - [ ] make more data fomat avalible to use for algorithm engineer such like ".json", ".pickle", ".xml", and etc.

The improvements of other algorithm to finish:
1. - [ ] abstract some data processing methods from industrial project and construct our own pipeline for processing data with mass trouble, which cannot be utilized by engineers directly
2. - [ ] add some models to construct the baseline for some practical applications, which include machine learning such like Regression tasks or Classification tasks, and operation research such like Planning Optimization tasks or Scheduling Optimization tasks. 