import  unittest
from similarityprocessorByTitle import similarprocessorByTitle as SimilarityProcessor
from DistanceAlgorithmType import DistanceAlgorithmType
from product import Product
class similarityprocessorByTitleTest(unittest.TestCase):

    def test_forcoffee(self):
        output = dict()
        similarity = SimilarityProcessor(True)
        output = similarity.getTopSimilarTextItems("A034",12,DistanceAlgorithmType.Levenshtein)

        for key in output.items():
            print(key[0].title)


if __name__ == '__main__':
    unittest.main()