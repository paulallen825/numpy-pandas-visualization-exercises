import pandas as pd
import numpy as np

from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/{employees}'