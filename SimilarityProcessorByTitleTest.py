import  unittest
from similarityprocessorByTitle import SimilarProcessorByTitle as SimilarityProcessor
from DistanceAlgorithmType import DistanceAlgorithmType
from product import Product
class SimilarityProcessorByTitleTest(unittest.TestCase):

    def test_forcoffee(self):
        output = dict()
        similarity = SimilarityProcessor(True)
        output = similarity.gettopsimilartextItems("A034", 4, DistanceAlgorithmType.Levenshtein)

        for key in output.items():
            print(key[0].title)


if __name__ == '__main__':
    unittest.main()