# --------------------------------------------------------------------------------------------------------
# -------------------- All libraries, variables and functions are defined in this file -------------------
# --------------------------------------------------------------------------------------------------------
# 1. libraries and instance of MongoDB ------------------------------------------------------------------/
from python_package.constants import * # constants

# a-1) import dependencies
from pymongo import MongoClient
from pprint import pprint
import pandas as pd
import json

# b-1)
# Create an instance of MongoClient
mongo=MongoClient(port=27017)
# confirm that our new database was created
print(f"""List of Available Database: {mongo.list_database_names()}""")
# -------------------------------------------------------------------------------------------------------/

# 2. function definition --------------------------------------------------------------------------------/
#a-2) sort parameter
def set_param( degree_search, tag): 
        add = [i+degree_search for i in tag]
        sub = [i-degree_search for i in tag]
        return (add,sub)
# -------------------------------------------------------------------------------------------------------/
