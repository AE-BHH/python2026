try:
    from . import cowsay
except ImportError:
    import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.dragon("Hello, " + sys.argv[1])
