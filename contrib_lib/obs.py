from ifm import Enum

"""
Extension child-class for IFM contributor's Extensions.
Use this class to add functionality relating to OBSERVATION POINTS.
Note: Functionality relating to the Observation Time Series should be implemented in the
      .hist class of this project.
"""

from .obs_geopandas import ObsGpd


class Obs:
    """
    Functions for working with observation point properties.
    """

    def __init__(self, doc):
        self.doc = doc

        # dictionary with reference values
        self.reference_values = {}

        # add custom child-classes here
        self.gdf = ObsGpd(doc)

    # add custom methods here

    def add_reference_values(self, refvalues, par=Enum.P_HEAD):
        """
        Adds reference values for the observation points
        :param refvalues: dictionary {label : value} with observed values
        :type refvalues: dict
        :param par: parameter to be set. (only Enum.P_HEAD implemented at the moment)
        :return: None
        """

        if type(refvalues) != dict:
            raise TypeError("refvalues must be of type dict")

        self.reference_values[par] = refvalues

    def plot_scatter(self, par=Enum.P_HEAD, labels=True, reference_line=True, format_plot=True,  *args, **kwargs):
        """
        Create a scatter plot
        :param par:
        :param add_labels:
        :param args:
        :param kwargs:
        :return: None
        """

        import matplotlib.pyplot as plt

        # abort if reference values do not exist
        if not par in self.doc.c.obs.reference_values.keys():
            raise ValueError("reference values not set. Use doc.c.obs.add_reference_values() first.")

        # get observation points
        gdf_obs = self.doc.c.obs.gdf.obspoints()

        # plot reference line
        hmin = min(gdf_obs.h_obs.min(), gdf_obs.h.min())
        hmax = max(gdf_obs.h_obs.max(), gdf_obs.h.max())
        if reference_line:
            plt.plot((hmin, hmax), (hmin, hmax), "grey")

        # create scatter plot
        plt.scatter(gdf_obs.h_obs, gdf_obs.h)

        # add lables
        if labels:
            for i, row in gdf_obs.iterrows():
                plt.annotate(s=row.label,
                             xy=(row.h_obs, row.h),
                             )
        # formatting
        if format_plot:
            plt.axis("equal")
            plt.xlabel("observed head [m]")
            plt.ylabel("modelled head [m]")
            plt.xlim(hmin, hmax)
            plt.ylim(hmin, hmax)

    def metrics(self):
        """
        Returns some common metrics of the calibration.
        :return: dictionary with metrics
        :rtype: dict
        """
        # get obspoints
        gdf_obs = self.doc.c.obs.gdf.obspoints()
        n = gdf_obs.h_res.count()

        # calculate metrics
        Phi = (gdf_obs.h_res ** 2).sum()  # Sum of squares
        RMSE = ((1. / n) * Phi) ** 0.5  # Residual mean squares
        E = gdf_obs.h_res.abs().mean()  # Mean absolute error

        return {"Phi": Phi,
                "RMSE": RMSE,
                "MAE": E}
