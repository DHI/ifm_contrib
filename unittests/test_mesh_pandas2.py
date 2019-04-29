import unittest
import ifm_contrib as ifm
from ifm import Enum


class TestMeshPd(unittest.TestCase):

    def test_elements(self):
        ifm.forceLicense("Viewer")
        doc = ifm.loadDocument("./models/example_2D.fem")
        df = doc.c.mesh.df.elements([Enum.P_TRANS])
        self.assertAlmostEqual(df[Enum.P_TRANS].sum(), 741.2000004276633)
        doc.c.mesh.df.elements(par=Enum.P_TRANS)   # 0
        doc.c.mesh.df.elements(par=[Enum.P_TRANS])  # 0
        doc.c.mesh.df.elements(par={"Transmissivity": Enum.P_TRANS})  # 0
        doc.c.mesh.df.elements(par=[Enum.P_TRANS], expr="elemental_expr_test")
        doc.c.mesh.df.elements(par=[Enum.P_TRANS], expr=["elemental_expr_test"])
        doc.c.mesh.df.elements(par=[Enum.P_TRANS], expr=["elemental_expr_test"], distr="elemental_test")
        doc.c.mesh.df.elements(par=[Enum.P_TRANS], expr=["elemental_expr_test"], distr=["elemental_test"])
        doc.c.mesh.df.elements(par=[Enum.P_TRANS], layer=1)  # 0

    def test_nodes(self):
        ifm.forceLicense("Viewer")
        doc = ifm.loadDocument("./models/example_2D.fem")
        doc.c.mesh.df.nodes(par=Enum.P_HEAD)   # 0
        doc.c.mesh.df.nodes(par=[Enum.P_HEAD])  # 0
        doc.c.mesh.df.nodes(par={"Head": Enum.P_HEAD})  # 0
        doc.c.mesh.df.nodes(par=[Enum.P_HEAD], expr="nodal_expr_test")
        doc.c.mesh.df.nodes(par=[Enum.P_HEAD], expr=["nodal_expr_test"])
        doc.c.mesh.df.nodes(par=[Enum.P_HEAD], expr=["nodal_expr_test"], distr="nodal_test")
        doc.c.mesh.df.nodes(par=[Enum.P_HEAD], expr=["nodal_expr_test"], distr=["nodal_test"])
        doc.c.mesh.df.nodes(par=[Enum.P_HEAD], slice=1)  # 0
        # self.assertAlmostEqual(df[Enum.P_TRANS].sum(), 741.2000004276633)

    def test_availableitems(self):
        ifm.forceLicense("Viewer")
        doc = ifm.loadDocument("./models/example_2D.fem")
        doc.c.mesh.df.get_available_items()
