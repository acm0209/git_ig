import sys

sys.path.append('secret/settings')

import config

print(config.DATABASE_CONFIG['dbname'])



