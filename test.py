from edit import EditUi
from Setting import SettingUi
from listui import  listUi
import sys
# import functools
import numpy as np
from datetime import date
import pandas as pd
from qt_material import apply_stylesheet
from encrypt import *
from schedule import *
from tray import TrayIcon
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from system_hotkey import SystemHotkey
from PyQt5.QtCore import QObject,pyqtSignal
from listwindowAdd import listwindowAddUi
from style import addstyle
from sqlalchemy import create_engine
from sqlalchemy import text

from sqlalchemy.types import DATE,CHAR,VARCHAR,TEXT,DATETIME,INT
import urllib.parse
import pymysql
DTYPE={'uid':TEXT,'score':INT}
engine=create_engine('mysql+pymysql://root:dls123@127.0.0.1:3306/maido',echo=True)
df = pd.DataFrame([['a1', 1], ['a2', 4]], columns=['uid', 'score'])
df.to_sql('new_table',con=engine,if_exists='append',index=False,chunksize=50,dtype=DTYPE)
'''try:
	
	print(">>> All good.")
except Exception as e:
	print(">>> Something went wrong!")'''