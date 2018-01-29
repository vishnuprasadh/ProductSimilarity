# ProductSimilarity
For a given product dataset, given a SKU - the output will return the closest other products based on product title match.

The above can easily be enhanced to add more classification or dependant attribute and using models like PCA and LDA for further refinement. I will update this to add more conditional attributes and weightage in future.

<b> Installation </b>

As of now, you just need to install the basic nltk and sklearn libraries with python for us to get this working.

```
pip install nltk

pip install sklearn
```
Note: Use --upgrade depending on the version you have.

Outside of the above, if you want to enhance with stopwords you should run the following.
```
import nltk
nltk.download('stopwords')

```
