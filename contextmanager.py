class Open:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
    def __enter__(self):
        self.handle =open(self.filename, self.mode)
        return self.handle
    def __exit__(self,exe_type,exe_val,exe_tb):
        self.handle.close()

#with Open('test.txt','w') as fh:
#    print('Our test is complete!', file=fh)

import contextlib

@contextlib.contextmanager
def open_context_manager(filename,mode='r'):
    fh= open(filename,mode)
    yield fh
    fh.close()

with open_context_manager('test.txt','w') as fh:
    print('Our test is compete!!',file=fh)