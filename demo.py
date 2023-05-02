'''

import pickle
from datetime import datetime

idFile = open('ids.p','wb')
detail = [21212,datetime.now().strftime("%H:%M:%S")]
pickle.dump(detail,idFile)
idFile.close()
print(detail)
'''

from subprocess import Popen

cmd = "python rough.py"
p = Popen(cmd, shell=True)
print(p)