import pandas as pd
from Engine.productModel import ProductModel
from Engine.textutils import TextUtils
import nltk
from collections import OrderedDict
from Engine.DistanceAlgorithmType import DistanceAlgorithmType
import os

'''
    This is the Object  which will be called by services that need to pull similar items.
    The logic is based on the title of the product alone using the Levenshtein distance algorithm.
    We can easily add more logic here to customize based on other parameters
    
    @@gettopsimilartextItems is to be used for getting the closest items for a given SKU.
'''
class SimilarProcessorByTitle:

    #Dataset against which we will need to put similarity quotient.
    data = pd.DataFrame()
    #baseItem against which we compare.
    baseItem = None

    '''
    By default default data will not be initialized. 
    In case @@loaddefault param is set to true, then a local sampledata.csv will be loaded.
    There is strong binding on excel format as follows where "," is demlimiter used:
    sku,brand,title,category,url,price,margin
    '''
    def __init__(self, loaddefault=False,data=None):
        if loaddefault and data==None:
            print( os.path.join(os.path.abspath(os.path.curdir), 'Engine/data/sampledata.csv'))
            self.data = pd.read_csv( os.path.join( os.path.abspath(os.path.curdir), 'Engine/data/sampledata.csv'),delimiter=',',header='infer')
        elif loaddefault:
            self.data = data


    '''
    Pass the SKU for which you want to find similar items and also pass an optional parameter of TopN.
    TopN - Sets value for the function that provides the output of N closest matching items. Default is 10.
    Returns the list of all Products as per @Product model. Key would have @Product model and value would have the distance.
    The order for distance will be from low to high which means closest to farthest.
    '''
    def gettopsimilartextItems(self, inputSKU="A034", topN=10, algo=DistanceAlgorithmType.Levenshtein):
        filteredData = []
        #Set the data for given SKU
        item = self.__getItemDataGivenSKU(inputSKU);

        if item:
            #Get the filtered data for the category of InputSKU
            filteredData = self.__getfilteredcategoryitemdata(item)
            #Get sorted list of items filtered by TopN
            filteredData = self.__calculatesimilarity(baseItem=item, filteredCategoryData=filteredData, topN=topN, algo=algo)

        self.baseItem = None
        self.data = None

        return filteredData


    'Given SKU load the baseItem data as a @Product domain object and return the object.'
    def __getItemDataGivenSKU(self,inputSKU):
        #if data is already loaded
        if not self.data.empty:
            self.baseItem = self.data.loc[self.data["sku"] == inputSKU]
        #Implement the backend call to return baseItem data as dataframe
        else:
            #load data for the given SKU and set the baseItem
            self.baseItem = None
        return self.__initializebaseitemdata()

    'Creates the @Product domain model once baseItem data is set. If  empty then returns None'
    def __initializebaseitemdata(self):
        rootItem = None
        # if base item exists
        if not self.baseItem.empty:
            # Get the root or base SKU item details against which we need to compare.
            rootItem = ProductModel.populate(self.baseItem)

        return rootItem

    '''
    Get the filtered category item data for the given Item
    '''
    def __getfilteredcategoryitemdata(self, rootItem):
        if self.data.empty:
            #Make call to load the  data for the given SKU
            self.data = None
        #Uses the local default data here.
        else:
            # filter all items which are from category we selected and not equal to inputSKU
            self.data = self.data[(self.data["category"] == rootItem.category) & (self.data["sku"] != rootItem.sku)]
            print('Items filtered for {} and Sku {}'.format(rootItem.category, rootItem.sku))

        return self.data


    '''
    For given baseItem, filtered category data and topN items the function returns a sorted closest "N" times agaisnt the baseitem.
    This function uses by default Levenshtein algorithms.
    We can also set to other options in future.
    '''
    def __calculatesimilarity(self, baseItem, filteredCategoryData, topN, algo):
        allitems = dict()
        # For each item which is in fitleredData
        for item in filteredCategoryData.iterrows():
            currentItem = ProductModel.populate(item[1])
            currentItem.title = TextUtils.CleanText(currentItem.title)
            #Get the Source category and Title.
            if algo == DistanceAlgorithmType.Levenshtein:
                allitems[currentItem] = nltk.edit_distance(baseItem.title, currentItem.title)
            elif algo == DistanceAlgorithmType.Binary:
                allitems[currentItem] = nltk.binary_distance(baseItem.title,currentItem.title)
        print("Base title is {}".format(baseItem.title))
        #Here also filter by topN and return
        return  OrderedDict(sorted(allitems.items(),key= lambda k : k[1] )[:topN])


if __name__ == '__main__':
    for sku in ["A034", "A018", "A021"]:
        similar = SimilarProcessorByTitle(True)
        items1 = similar.gettopsimilartextItems(sku, 5, DistanceAlgorithmType.Levenshtein)
        for key in items1.items():
            print(key[0].title)
        print("--------------completed for levenshtein-----------\n")

    for sku in ["A039", "A007", "A013"]:
        similar2 = SimilarProcessorByTitle(True)
        items1 = similar2.gettopsimilartextItems(sku, 5, DistanceAlgorithmType.Levenshtein)
        for key in items1.items():
            print(key[0].title)
        print("--------------completed for Binary-----------\n")
