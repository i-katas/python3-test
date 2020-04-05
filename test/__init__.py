import sys, io
from os import path

config_file = path.join(path.dirname(__file__), '../setup.cfg')

class mock_stderr(): 
    def __enter__(self) -> io.StringIO():
        self._stderr, sys.stderr = sys.stderr, io.StringIO()
        return sys.stderr
    def __exit__(self, *args):
        sys.stderr = self._stderr
        del self._stderr

__path__.append('foo')
