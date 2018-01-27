class Product:

    sku, title, brand, category, url, price, margin, kwargs = "","","","","",None,None,None

    def __init__(self):
        print("Initialized basic product")

    def __init__(self, sku, title, brand, category, url, price,margin,**kwargs):
        self.sku = sku
        self.title = title
        self.brand = brand
        self.category = category
        self.url = url
        self.price = price
        self.margin = margin
        self.kwargs = kwargs
        print("Initialized with all base attribute set")
