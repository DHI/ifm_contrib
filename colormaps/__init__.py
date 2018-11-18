from matplotlib.colors import LinearSegmentedColormap
import numpy as np

feflow_rainbow = LinearSegmentedColormap.from_list("feflow_rainbow",
                                                   np.array([[0.5, 0.0, 0.5, 1.0],
                                                     [0.0, 0.0, 1.0, 1.0],
                                                     [0.0, 0.75, 0.75, 1.0],
                                                     [0.0, 1.0, 0.0, 1.0],
                                                     [1.0, 1.0, 0.0, 1.0],
                                                     [1.0, 0.0, 0.0, 1.0]]),
                                                   N=100)

# xmlfile = "./feflow_rainbow.xml"
# colors = []
# lines = open(xmlfile).readlines()
# for line in [l for l in lines if "colorItem frac" in l]:
#     words = [w.split("=")[-1].strip('"') for w in line.split()]
#     wfrac = float(words[1])
#     wr = float(words[2])
#     wg = float(words[3])
#     wb = float(words[4])
#     wa = float(words[5])
#     colors.append([wr, wg, wb, wa])