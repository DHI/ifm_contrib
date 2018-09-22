from ifm import Enum
from .hist_pandas import HistPd


class Hist:
    """
    Extension child-class for IFM contributor's Extensions.
    Use this class to add functionality relating to OBSERVATION HISTORIES.
    Note: Functionality relating to the Observation Points (e.g. Geometry) should be implemented in the
          .obs class of this project.
    """

    def __init__(self, doc):
        self.doc = doc

        # add custom child-classes here
        self.df = HistPd(doc)

    # add custom methods here
