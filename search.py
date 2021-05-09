import tkinter as tk
import os
import tempfile
root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
label2 = tk.Label(root, text='Path')
label1 = tk.Label(root, text='Query')
canvas1.create_window(200, 160, window=entry1)
canvas1.create_window(200, 140, window=label1)
canvas1.create_window(200, 100, window=label2)
canvas1.create_window(200, 120, window=entry2)

def letsGO():
    file_path = os.path.join(tempfile.gettempdir(), 'txt.search-ms')
    q = entry1.get()
    text=""
    text2=""
    path=entry2.get()
    c = q.split("OR")
    for y in range(len(c)):
        text=text+'<condition type="leafCondition" property="" operator="imp" propertyType="string" value="'+c[y]+'" localeName="en-US"><attributes/></condition>'
    for y in range(len(c)):
        text2=text2+'<condition type="leafCondition" property="System.Generic.String" operator="wordmatch" propertyType="string" value="' +c[y] + '" localeName="en-US"> <attributes> <attribute attributeID="{9554087B-CEB6-45AB-99FF-50E8428E860D}" clsid="{C64B9B66-E53D-4C56-B9AE-FEDE4EE95DB1}" chs="1" sqro="585" timestamp_low="1021899861" timestamp_high="30881614"> <condition type="leafCondition" property="System.Generic.String" operator="wordmatch" propertyType="string" value="' +c[y] + '" localeName="en-US"> <attributes> <attribute attributeID="{9554087B-CEB6-45AB-99FF-50E8428E860D}" clsid="{C64B9B66-E53D-4C56-B9AE-FEDE4EE95DB1}" chs="1" sqro="585" timestamp_low="887889061" timestamp_high="30881614"> <condition type="leafCondition" property="" operator="imp" propertyType="string" value="' +c[y] + '" localeName="en-US"> <attributes /> </condition> </attribute> </attributes> </condition> </attribute> </attributes> </condition>'

    dt1 = r"""<?xml version="1.0" encoding="UTF-8"?> <persistedQuery version="1.0"> <viewInfo viewMode="icons" iconSize="96" stackIconSize="0" displayName="Search ResGYUYU foto" autoListFlags="0"> <visibleColumns> <column viewField="System.ItemNameDisplay" /> <column viewField="System.ItemDate" /> <column viewField="System.Keywords" /> <column viewField="System.Size" /> <column viewField="System.Rating" /> <column viewField="System.ItemFolderPathDisplay" /> </visibleColumns> <sortList> <sort viewField="System.Search.Rank" direction="descending" /> <sort viewField="System.ItemDate" direction="descending" /> <sort viewField="System.ItemNameDisplay" direction="ascending" /> </sortList> </viewInfo> <query> <conditions> <condition type="orCondition"> <attributes> <attribute attributeID="{9554087B-CEB6-45AB-99FF-50E8428E860D}" clsid="{C64B9B66-E53D-4C56-B9AE-FEDE4EE95DB1}" chs="1" sqro="585" timestamp_low="341906207" timestamp_high="30881744"> <condition type="orCondition"> <attributes> <attribute attributeID="{9554087B-CEB6-45AB-99FF-50E8428E860D}" clsid="{C64B9B66-E53D-4C56-B9AE-FEDE4EE95DB1}" chs="0" parsedString="GS__3495 OR GS__3496" localeName="en-US" timestamp_low="102886515" timestamp_high="30881744"/> </attributes>"""
    dt2 = r"""</condition></attribute></attributes>"""
    dtpath = '</condition> </conditions> <kindList> <kind name="item" /> </kindList> <scope> <include path="'+path+'" attributes="1887437183" /> </scope> </query> <properties> <author Type="string">ADDDDor</author> </properties> </persistedQuery>'
    txtfin=dt1+text+dt2+text2+dtpath
    m=open(file_path, 'w+')
    m.write(txtfin)
    m.close
    os.system('start /B start cmd.exe @cmd /k '+file_path+'')
button1 = tk.Button(text='Oke', command=letsGO)
canvas1.create_window(200, 180, window=button1)

root.mainloop()