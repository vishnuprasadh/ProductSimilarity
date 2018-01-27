import  unittest
from similarityprocessorByTitle import similarprocessorByTitle as SimilarityProcessor
from product import Product
class similarityprocessorByTitleTest(unittest.TestCase):

    def test_forcoffee(self):
        output = dict()
        similarity = SimilarityProcessor(True)
        output = similarity.getTopSimilarTextItems("A032",12)

        for key in output.items():
            print(key[0].title)


if __name__ == '__main__':
    unittest.main()