import pandas as pd
import folium
from folium.plugins import MarkerCluster
from folium import plugins
datafile = "382019_aed.csv"
lat, lon =33.8130772, 132.7587632
zoom_start = 18


webfile_name = "c2.html"

m = folium.Map(location=[lat, lon], zoom_start=zoom_start,)

marker_cluster = plugins.MarkerCluster().add_to(m)

X = pd.read_csv(datafile)
for index, r in X.iterrows(): 
    p = '<div id="q"><h2>名称 : %s</h2><br><h3>設置場所 : %s</h3><hr><a href="https://www.google.co.jp/maps?q=%f,%f">マップ : %s</a><br></div>' % (r.名称,r.設置位置,r.緯度, r.経度,r.所在地) 
    folium.Marker([r.緯度, r.経度], popup=p,icon=folium.Icon(color='red', icon='flash')).add_to(marker_cluster)


m.save(webfile_name)

#white-space: nowrap;