# --------------------------------------------------------------------------------------------------------
# ------------------------------------------------ Classes -----------------------------------------------
# --------------------------------------------------------------------------------------------------------

# 1. dependencies and setup -----------------------------------------------------------------------------/
from python_package.helpers import *  # liberaries and functions
# -------------------------------------------------------------------------------------------------------/

# 2. defining new data insert class ---------------------------------------------------------------------/
class New_Data():
    def __init__(self, file, collection, tag):
        self.file       = file
        self.collection = collection
        self.tag        = tag

    def set_file(self):
        with open(RESOURCE_PATH+self.file,"r") as new_data:
            self.file_data = json.load(new_data)
        self.index = self.file_data[0][self.tag]

    def get_file(self):
        return self.file_data

    def insert_file(self):
        # check to see if the value already exists in the database
        query={self.tag:{"$regex":self.index}}
        if len(list(self.collection.find(query))) > 0:
            print(f"{self.tag}: {self.index} already exists")
            return
        if isinstance(self.file_data, list):
            self.collection.insert_many(self.file_data) 
        else:
            self.collection.insert_one(self.file_data)
    
    def drop_entry(self):
        self.collection.delete_many({self.tag:self.index})
# -------------------------------------------------------------------------------------------------------/

# 3. defining queries class -----------------------------------------------------------------------------/
class Queries():
    
    def __init__(self, collection, pipline ):
        self.pipline    = pipline
        self.collection = collection

    def set_result(self):
        var = len(self.pipline)
        if var == 0:
            print(WARNING_1)
            return
        elif var == 1:
            self.result=list(self.collection.find(self.pipline[0]))
        elif var == 2:
            self.result=list(self.collection.find(self.pipline[0],self.pipline[1]))
        elif var >2:
            self.result=list(self.collection.aggregate(self.pipline))
        self.counts=len(self.result)

    def get_result(self,limit=10):
        self.limit = limit
        print(DOC_COUNT+str(self.counts)+HORIZONTAL_LINE)
        pprint(self.result[0:self.limit])
    
    def drop_entry(self):
        self.collection.delete_many(self.pipline[0])
        # check if any remaining documents include query
        self.count=self.collection.count_documents(self.pipline[0])
        if self.count == 0:
            print(f"""All doucments with {self.pipline[0]} data deleted successfully""")
        # check that other documents remain with 'find_one'
        self.remain=self.collection.count_documents({})
        print(HORIZONTAL_LINE+"Remain documents with "+str(self.remain)+" counts"+HORIZONTAL_LINE)
        remain_doc=self.collection.find({})
        pprint(list(remain_doc)[0])
    
    def sort_limit(self, sort, ascending, limit):
        self.sort   = [(sort, ascending)]
        self.limit  = limit
        self.result = list(self.collection.find(self.pipline[0]).sort(self.sort).limit(self.limit))
        self.counts = len(self.result)
        print(DOC_COUNT+str(len(list(self.collection.find(self.pipline[0]).sort(self.sort))))+HORIZONTAL_LINE)
        print(LIMIT_ID+str(self.counts)+HORIZONTAL_LINE)
        pprint(self.result)

    def ConvertToDF(self,index=10):
        # convert the result to a Pandas DataFrame
        param_df=pd.DataFrame(self.result)
        # display the number of rows in the DataFrame
        number_of_rows=len(param_df)
        print(ROW_COUNT+str(number_of_rows)+HORIZONTAL_LINE)
        # display the first 10 rows of the DataFrame
        return param_df.head(index)
# -------------------------------------------------------------------------------------------------------/
