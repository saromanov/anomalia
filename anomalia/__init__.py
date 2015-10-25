import sys
__version__ = 0.1

if sys.version_info < (3,3):
    print("Anomalia {0} requires Python 3.3".format( __version__))
    sys.exit(1)
