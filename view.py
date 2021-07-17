import eel
from pandas.core import series
import desktop
import search
import pandas as pd

app_name="html"
end_point="index.html"    #確認なし
size=(700,600)


# 検索処理呼び出し
@ eel.expose
def kimetsu_search(filename, word):
    search.kimetsu_search(filename, word)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)