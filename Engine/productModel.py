from Engine import product as p
import pandas as pd

class ProductModel:

    'Pass the @itemData as series object to this function which returns the product model'
    def populate(itemData):
        product = None
        if type(itemData) is pd.DataFrame:
            product = p.Product (sku=itemData["sku"].iloc[0],
                      title=itemData["title"].iloc[0],
                      brand=itemData["brand"].iloc[0],
                      category=itemData["category"].iloc[0],
                      url=itemData["url"].iloc[0],
                      price=itemData["price"].iloc[0],
                      margin=itemData["margin"].iloc[0],
                      kwargs=""
                      )
        elif type(itemData) is pd.Series:
            product = p.Product(sku=itemData["sku"],
                                title=itemData["title"],
                                brand=itemData["brand"],
                                category=itemData["category"],
                                url=itemData["url"],
                                price=itemData["price"],
                                margin=itemData["margin"],
                                kwargs=""
                                )

        return product