from flask import Flask, request,Request,jsonify,abort,Blueprint
from Engine.similarityprocessorByTitle import SimilarProcessorByTitle as similarEngine
from Engine.product import Product

app = Flask(__name__)

@app.route('/productsimilarity/<sku>/<top>')
def getsimilarproducts(sku,top):
    error  = None
    response = {}

    try:
        if top == None or top=="": top = 10
        similarity = similarEngine(True)
        data = similarity.gettopsimilartextItems(inputSKU=sku,topN=int(top))

        values = list()
        for key in data.items():
            values.append(
                    {
                        "sku": key[0].sku,
                        "category":key[0].category,
                        "title":key[0].title,
                        "url":key[0].url,
                        "brand": key[0].brand
                    }
                )
        response = jsonify(values)


        response.statuscode = 200
    except Exception as ex:
        response.statuscode = 400
        print(ex)
    finally:
        return response


if __name__ == '__main__':
    app.run(debug=True,port=8099,threaded=True)