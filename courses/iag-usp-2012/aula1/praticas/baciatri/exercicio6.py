import numpy
from fatiando.ui.gui import BasinTri
import cPickle as pickle


with open('exercicio6.pickle') as f:
    data = pickle.load(f)
    xp = data['xp']
    zp = data['zp']
    nodes = data['nodes'][0]
    gz = data['gz']
    density = data['density']

area = (0, 100000, 0, 5000)
xp = numpy.arange(0, 100000, 1000)
zp = numpy.zeros_like(xp)
app = BasinTri(area, nodes[0:2], xp, zp, gz)
app.densities[0] = density
app.run()

with open('exercicio6-modelo.pickle', 'w') as f:
    data = {'xp':xp, 'zp':zp, 'nodes':1000*numpy.array(app.polygons[0]),
            'gz':app.get_data(),
            'density':app.densities[0]}
    pickle.dump(data, f)
