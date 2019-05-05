import unittest
import ifm_contrib as ifm
# from ifm import Enum


class TestObsGpd(unittest.TestCase):

    def test_history(self):
        ifm.forceLicense("Viewer")
        doc = ifm.loadDocument("./models/example_2D.dac")

        # check if all_hist_itemsworks
        doc.c.hist.df.all_hist_items()

        # test history function
        from datetime import datetime
        doc.c.hist.df.history("HEAD", reference_time=datetime(2018, 1, 1))

        # test depreciated functions
        doc.c.hist.df.getDataframe("HEAD", reference_time=datetime(2018, 1, 1))

        # should return a certain number of entries
        self.assertEqual(46, len(doc.c.hist.df.HEAD))
