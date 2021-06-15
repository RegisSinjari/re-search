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
        a=c[y].replace("name:=","")
        text=text+'<condition type="leafCondition" property="System.ItemNameDisplay" operator="eq" propertyType="string" value="'+a+'" valuetype="System.StructuredQueryType.Blurb" localeName="en-US"> <attributes /> </condition>'
    for y in range(len(c)):
        a = c[y].replace("name:=", "")
        text2=text2+'<condition type="leafCondition" property="System.ItemNameDisplay" operator="eq" propertyType="string" value="'+a+'" localeName="en-US"> <attributes> <attribute attributeID="{9554087B-CEB6-45AB-99FF-50E8428E860D}" clsid="{C64B9B66-E53D-4C56-B9AE-FEDE4EE95DB1}" chs="1" sqro="585" timestamp_low="1042864196" timestamp_high="30892363"> <condition type="leafCondition" property="System.ItemNameDisplay" operator="eq" propertyType="string" value="README.txt" localeName="en-US"> <attributes> <attribute attributeID="{9554087B-CEB6-45AB-99FF-50E8428E860D}" clsid="{C64B9B66-E53D-4C56-B9AE-FEDE4EE95DB1}" chs="1" sqro="585" timestamp_low="955327362" timestamp_high="30892363"> <condition type="leafCondition" property="System.ItemNameDisplay" operator="eq" propertyType="string" value="README.txt" valuetype="System.StructuredQueryType.Blurb" localeName="en-US"> <attributes /> </condition> </attribute> </attributes> </condition> </attribute> </attributes> </condition>'

    aba="::{20D04FE0-3AEA-1069-A2D8-08002B30309D}\\"+path
    odt1=r"""<?xml version="1.0" encoding="UTF-8"?> <persistedQuery version="1.0"> <viewInfo iconSize="32" stackIconSize="0" displayName="Search Results in adin" autoListFlags="0"> <visibleColumns> <column viewField="System.ItemNameDisplay" /> <column viewField="System.DateModified" /> <column viewField="System.ItemTypeText" /> <column viewField="System.Size" /> <column viewField="System.ItemFolderPathDisplayNarrow" /> </visibleColumns> <sortList> <sort viewField="System.Search.Rank" direction="descending" /> <sort viewField="System.DateModified" direction="descending" /> <sort viewField="System.ItemNameDisplay" direction="ascending" /> </sortList> </viewInfo> <query> <conditions> <condition type="orCondition"> <attributes> <attribute attributeID="{9554087B-CEB6-45AB-99FF-50E8428E860D}" clsid="{C64B9B66-E53D-4C56-B9AE-FEDE4EE95DB1}" chs="1" sqro="585" timestamp_low="1042864196" timestamp_high="30892363"> <condition type="orCondition"> <attributes>"""
    odt2 ='<attribute attributeID="{9554087B-CEB6-45AB-99FF-50E8428E860D}" clsid="{C64B9B66-E53D-4C56-B9AE-FEDE4EE95DB1}" chs="0" parsedString="'+q+'" localeName="en-US" timestamp_low="955317403" timestamp_high="30892363" /> </attributes>'
    dtpath=r'</condition> </conditions> <kindList> <kind name="item" /> </kindList> <scope> <include path="'+aba+'" attributes="1887437183" /> attributes="1887437183" /> </scope> </query> <properties> <author Type="string">Administrator</author> </properties> </persistedQuery>'

    txtfin=odt1+odt2+text+'</condition></attribute></attributes>'+text2+dtpath
    m=open(file_path, 'w+')
    m.write(txtfin)
    m.close
    os.system('start /B start cmd.exe @cmd /k '+file_path+'')
button1 = tk.Button(text='Oke', command=letsGO)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
