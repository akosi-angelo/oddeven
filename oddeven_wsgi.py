import sys
path = '/home/angeloprogrammer/oddeven'
if path not in sys.path:
    sys.path.append(path)

from oddcheck import app as application
