import pyexcel
from collections import OrderedDict
#2 data
data = [
    OrderedDict({
        "Name": "quan",
        "age": 24,
    }),
    OrderedDict({
        "Name": "duc",
        "age": 26,
    }),
]
# list comprehension
#3 save
pyexcel.save_as(records=data, dest_file_name="xample.xls")