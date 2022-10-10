import streamlit as st
import pandas as pd
import numpy as np
import pickle
loaded_model= pickle.load(open('model.pkl' , 'rb'))

@st.cache
def predict_result(input_data):
  input_array = np.asarray(input_data)
  reshape_input = input_array.reshape(1,-1)

  prediction = loaded_model.predict(reshape_input)
  if prediction == 0:
    return " Insurance quote is accepted"
  return " Insurance quote is not accepted"

def main():
  st.title("Insurance acceptance based on quote")
  QuoteNumber = st.text_input("Enter Quote Number")
  Field6 = st.selectbox('select field6:',['A','B','C','D','E','F','J','K'],key=20)
  Field7 =  st.selectbox('selectfield7:',
['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28'],key=22)
  Field8 = st.slider('select field8:', 0.8700,1.1000,step=0.5)
  Field9 =st.selectbox('select field9:',['0.0038','0.0040','0.0004','0.0006','0.0007'],key=24)
  Field10 = st.selectbox('select field 10:', ['935','1113','965','548','564','1165','1487','1480'],key=25)
  Field11 = st.selectbox('select field 11:',['1.0200','1.2665','1.3045','1.1886','1.2433','1.2694','1.0670','1.1161','1.2714','1.2392','1.0000'],key=26)
  Field12 = st.selectbox('select field 12:',['N','Y'],key=27)
  CoverageField1A = st.slider('select Coveragefield1A:', -1,25,step=1)
  CoverageField5A = st.selectbox('select Coveragefield 5A:',['1','13','25'],key=29)
  CoverageField5B =  st.selectbox('select Coveragefield 5B:',['1','2','22','25'],key=30)
  CoverageField6A =  st.selectbox('select Coveragefield 6A:',['1','13','25'],key=31)
  CoverageField6B = st.selectbox('select Coveragefield 6B:',['1','6','23','25'],key=32)
  CoverageField8 =  st.selectbox('select Coveragefield 8:',['T','U','V','W','X','Y','Z'],key=33)
  CoverageField9 =  st.selectbox('select Coveragefield 9:',['A','B','C','D','E','F','G','H','I','J','K','L'],key=34)
  CoverageField11A = st.slider('select Coveragefield11A:', -1,25,step=1)
  SalesField1A = st.slider('select Salesfield1A:', 1,25,step=1)
  SalesField1B =  st.slider('select SalesField1B:', 1,25,step=1)
  SalesField2A = st.slider('select SalesField2A:', -1,25,step=1)
  SalesField2B = st.slider('select SalesField2B:', -1,25,step=1)
  SalesField3 = st.selectbox('select Salesfield3:',['1','0'],key=40)
  SalesField4= st.selectbox('select Salesfield 4:',['1','2','3','4','5'],key=41)
  SalesField5= st.selectbox('select Salesfield 5:',['1','2','3','4','5'],key=42)
  SalesField6 =  st.slider('select SalesField6:', 1,24,step=1)
  SalesField7 =  st.selectbox('select Salesfield 7:',['K','P','T','Q','V','R','M'],key=44)
  SalesField8 =  st.number_input('Enter value between 0-260752')
  SalesField9 = st.selectbox('select Salesfield9:',['1','0'],key=46)
  SalesField10 =  st.slider('select SalesField10:', 0,21,step=1)
  SalesField11 =  st.selectbox('select Salesfield11:',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28'],key=48)
  SalesField13= st.selectbox('select Salesfield 13:',['1','2','3','4','5','6','7'],key=49)
  SalesField14= st.selectbox('select Salesfield 14:',['1','2','3','4','5','6','7','8','9','11','14'],key=50)
  PersonalField1 = st.selectbox('select personalfield1:',['1','0'],key=51)
  PersonalField4A = st.slider('select Personalfield4A:', -1,25,step=1)
  PersonalField5 = st.selectbox('select Personalfield 5:',['1','2','3','4','5','6','7','9','10'],key=53)
  PersonalField6 = st.selectbox('select personalfield6:',['1','0'],key=54)
  PersonalField7 = st.selectbox('select personalfield7:',['N','Y','UNKNOWN'],key=55)
  PersonalField8 = st.selectbox('select personalfield8:',['1','2','3'],key=56)
  PersonalField9 = st.selectbox('select personalfield9:',['1','2','3'],key=57)
  PersonalField10A = st.slider('select personalfield10A:', -1,25,step=1)
  personalField11 = st.selectbox('select personalfield11:',['0','1','2','3','4'],key=59)
  personalField12 = st.selectbox('select personalfield12:',['1','2','3','4','5'],key=60)
  personalField13 = st.selectbox('select personalfield13:',['1','2','3','4'],key=61)
  personalField14 = st.selectbox('select personalfield14:',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','18','19','20','21','22','23','25','30','32','35','47','50','52','54'],key=62)
  PersonalField15 =  st.selectbox('select Salesfield11:',['1','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','24'],key=63)
  personalfield16 = st.selectbox('select personalfield16:',['ZA','XR','XJ','XM','XD','XH','XX','XO','XB','YH','ZH','ZT','ZF','ZR','XS','ZN','YF','YE','ZG','XW','XQ',
'ZW','XE','ZC','XC','ZK','XI','ZD','ZE','XZ','ZJ','XL','XP','ZU','YI','XK','XF','ZB','XN','ZI','XT','ZV','XU','XV','ZO','ZQ','XY','ZS','ZP','ZL'],key=65)
  PersonalField17 = st.selectbox('select personalfield17:',['XB','XC','XD','XE','XG','XH','XI','XJ','XK','XL','XM','XN', 'XO','XP','XQ','XR','XS','XT','XU' 'XV','XW','XX','XY','YE','YF','YG','YH','YI','YJ','YK','YL','YM','YN','YP','YQ','YR','YS','YT','YU','YV','YW', 'YX','YY','YZ', 'ZA','ZB','ZC',
'ZD','ZE','ZF','ZG','ZH','ZI','ZK','ZL','ZM','ZN','ZO','ZP','ZQ','ZR','ZS','ZT','ZU','ZV','ZW'],key=67)
  PersonalField18 = st.selectbox('select personalfield18:',['XC','XD','XE','XF','XG','XH','XI','XJ','XK','XL','XM','XN','XO','XP','XQ','XR','XS','XT','XU',
'XV','XW','XX','XY','XZ','YE','YF','YG','YH','YI','YJ','YK','YL','YM','YN','YO','YP','YQ','YR','ZA','ZB','ZC','ZD','ZE','ZF','ZG','ZH','ZI','ZJ','ZK','ZL',
'ZM','ZN','ZO','ZP','ZQ','ZR','ZS','ZT','ZU','ZV','ZW'],key=70)
  personalfield19 = st.selectbox('select personalfield19:',['XC','XD','XE','XF','XG','XH','XI','XJ','XK','XL','XM','XN','XO','XP','XQ','XR','XS','XT','XU',
'XV','XW','XX','XY','XZ','YE','YF','YG','YH','YI','YJ','YK','YL','YM','YN','ZA','ZB','ZC','ZD','ZE','ZF','ZG','ZH','ZI','ZJ','ZK','ZL',
'ZM','ZN','ZO','ZP','ZQ','ZR','ZS','ZT','ZU','ZV','ZW'],key=73)
  PersonalField5 = st.selectbox('select Personalfield 5:',['1','2','3','4','5','6','7','9','10'],key=74)
  PersonalField27 = st.selectbox('select Personalfield 27:',['0','1','2','3','4','5','6','7','9','10','11','12','13','14','15'],key=75)
  PersonalField28 = st.selectbox('select Personalfield 28:',['1','2','3','4','5','6','7'],key=76)
  PersonalField29 = st.selectbox('select Personalfield 29:',['1','2','3','4','5','6','7'],key=77)
  PersonalField30 = st.selectbox('select Personalfield 30:',['0','1','2','3','4','5','6','7','10','14','22'],key=78)
  PersonalField31 = st.selectbox('select Personalfield 31:',['0','1','2','3','4','5','6','7','9','11','15','23'],key=79)
  PersonalField34 = st.selectbox('select Personalfield 34:',['1','2','3','4','5','6','7'],key=80)
  PersonalField39 = st.selectbox('select Personalfield 39:',['0','1','2','3','4','5','6','7','8'],key=81)
  PersonalField40 = st.selectbox('select Personalfield 40:',['0','1','2','3','4','5','6','7','8','9'],key=82)
  PersonalField49 = st.selectbox('select Personalfield 49:',['0','1','2','3','4','6','7'],key=83)
  PersonalField54 = st.selectbox('select Personalfield 54:',['0','1','2','3','4','5','6','7','8','10','12'],key=84)
  PersonalField59 = st.selectbox('select Personalfield 59:',['0','1','2','3','4','5','6'],key=85)
  PersonalField64 = st.selectbox('select Personalfield 64:',['0','1','2'],key=86)
  PersonalField65 = st.selectbox('select Personalfield 65:',['0','1','2'],key=87)
  PersonalField66 = st.selectbox('select Personalfield 66:',['0','1','2'],key=88)
  PersonalField67 = st.selectbox('select Personalfield 67:',['0','1','2'],key=89)
  PersonalField69 = st.selectbox('select Personalfield 69:',['0','1','2','3','4','5'],key=90)
  PersonalField70 = st.selectbox('select Personalfield 70:',['0','1','2','3','4','5','7'],key=91)
  PersonalField74 = st.selectbox('select Personalfield 74:',['0','1','2','3','4','5','7','22'],key=92)
  PersonalField79 = st.selectbox('select Personalfield 79:',['0','1','2','3','4','5','7'],key=93)
  PersonalField84 = st.selectbox('select Personalfield 84:',['-99','1.0','2.0','3.0','4.0','5.0','7.0'],key=94)
  PropertyField1A = st.slider('select Propertyfield1A:', -1,25,step=1)
  PropertyField2A = st.slider('select Propertyfield2A:',['-1','25'])
  PropertyField2B = st.selectbox('select Propertyfield2B:',['15','8','12','13','10','9','23','2','3','4','6','24','20','5','18','19','25','21','16','17','22'],key=97)
  PropertyField3 = st.selectbox('select propertyfield3:',['N','Y','UNKNOWN'],key=98)
  PropertyField4 = st.selectbox('select propertyfield4:',['N','Y','UNKNOWN'],key=99)
  PropertyField5 = st.selectbox('select propertyfield5:',['N','Y'],key=100)
  PropertyField6 = 0
  PropertyField7 = st.selectbox('select propertyfield7:',['o','R','J','D','S','N','I','Q','A','K','H','E','L','F','G','M','P','C','B'],,key=102)
  PropertyField8 = st.selectbox('select propertyfield8:',['0','1'],key=103)
  PropertyField9 = st.selectbox('select propertyfield9:',['0','1','2'],key=104)
  PropertyField10 = st.selectbox('select propertyfield10:',['0','1','2','3','4'],key=105)
  PropertyField11A = st.slider('select Propertyfield11A:',['-1','25'])
  PropertyField11B = st.selectbox('select Propertyfield11B:',['21','22','23','24','25'],key=107)
  PropertyField12 = st.selectbox('select Propertyfield12:',['1','2','3','4','5','6','7'],key=108)
  PropertyField13 = st.selectbox('select Propertyfield13:',['0','1','2','3'],key=109)
  PropertyField14 = st.selectbox('select Propertyfield14:',['A','B','C','D'],key=110)
  PropertyField15 = st.selectbox('select Propertyfield15:',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],key=111)
  PropertyField16A = st.slider('select Propertyfield16A:', -1,25,step=1)
  PropertyField17 = st.selectbox('select Propertyfield17:',['0','1','2','3','4','5','6','7'],key=113)
  PropertyField18 = st.selectbox('select Propertyfield18:',['0','1','2','3','4','5','6','7','8','9'],key=114)
  PropertyField19 = st.selectbox('select Propertyfield19:',['0','1','2','3','4','5','6','7','8','9'],key=115)
  PropertyField20 = st.selectbox('select Propertyfield20:',['0','1','2'],key=116)
  PropertyField21A = st.slider('select Propertyfield21A:',-1,25,step =1)
  PropertyField22 = st.selectbox('select Propertyfield22:',['1','2','3','4','5'],key=118)
  PropertyField23 = st.selectbox('select Propertyfield23:',['1','2','3','4','5','6','7','8','9','10','11','13','14'],key=119)   
  PropertyField24A = st.slider('select Propertyfield24A:',-1,25,step =1)  
  PropertyField25 = st.selectbox('select Propertyfield25:',['0.0','1.0','1.5','2.0','2.5','3.0','3.5','4.0','5.0','6.0','7.0'],key=121)
  PropertyField26A = st.slider('select Propertyfield26A:',-1,25,step =1) 
  PropertyField27 = st.selectbox('select Propertyfield27:',['1','2','3','4','6','7','8','9','10','11','13','14','15','16','17','18','19'],key=123)
  PropertyField28 = st.selectbox('select Propertyfield28:',['A','B','C','D'],key=124)
  PropertyField29 = st.selectbox('select Propertyfield29:',['-99','0.0','1.0'],key=125)
  PropertyField30 = st.selectbox('select propertyfield5:',['N','Y'],key=126)
  PropertyField31 = st.selectbox('select Propertyfield31:',['o','K','N','M'],key=127)
  PropertyField32 = st.selectbox('select propertyfield32:',['Y','N','UNKNOWN'],key=128)
  PropertyField33 = st.selectbox('select Propertyfield33:',['H','G','E','F'],key=129)
  PropertyField34 = st.selectbox('select propertyfield34:',['Y','N','UNKNOWN'],key=130)
  PropertyField35 = st.selectbox('select propertyfield35:',['1','2','0'],key=131)
  PropertyField36 = st.selectbox('select propertyfield36:',['Y','N','UNKNOWN'],key=132)
  PropertyField37 = st.selectbox('select propertyfield37:',['Y','N','UNKNOWN'],key=1133)
  PropertyField38 = st.selectbox('select propertyfield38:',['Y','N','UNKNOWN'],key=134)
  PropertyField39A = st.slider('select Propertyfield39A:',-1,25,step =1)
  GeographicField1A = st.slider('select GeographicField1A:',-1,25,step =1)
  GeographicField2A = st.slider('select GeographicField2A:',-1,25,step =1)
  GeographicField3A = st.slider('select GeographicField3A:',1,25,step =1)
  GeographicField4A = st.slider('select GeographicField4A:',1,25,step =1)
  GeographicField5A = st.selectbox('select GeographicField5A:',['-1','25'],key=140)
  GeographicField5B = st.selectbox('select GeographicField5B:',['13','19','25','20','23','14','16','21','22','17','15','18','24','-1'],key=141)
  GeographicField6A = st.slider('select GeographicField6A:',-1,25,step =1)
  GeographicField6B = st.slider('select GeographicField6B:',-1,25,step =1)
  GeographicField7A = st.slider('select GeographicField7A:',-1,25,step =1)
  GeographicField10A = -1
  GeographicField10B = st.selectbox('select GeographicField10B:',['-1','25'],key=146)
  GeographicField14A = st.selectbox('select GeographicField14A:',['-1','25'],key=11225)
  GeographicField17A = st.slider('select GeographicField17A:',-1,25,step =1)
  GeographicField18A = st.selectbox('select GeographicField18A:',['-1','25'],key=149)
  GeographicField18B = st.slider('select GeographicField18B:',-1,25,step =1)
  GeographicField19A = st.slider('select GeographicField19A:',-1,25,step =1)
  GeographicField20A = st.slider('select GeographicField20A:',-1,25,step =1)
  GeographicField20B = st.slider('select GeographicField20B:',-1,25,step =1)
  GeographicField21A = st.selectbox('select GeographicField21A:',['-1','25'],key=154)
  GeographicField21B = st.selectbox('select GeographicField21B:',['4','22','6','24','9','11','20','7','25','16','17','15','12','14','18','10','13','19','8','23','5','21','-1'],key=155)
  GeographicField22A = st.selectbox('select GeographicField22A:',['-1','25'],key=156)
  GeographicField22B = st.selectbox('select GeographicField22B:',['15','19','20','22','25','23','16','18','21','14','17','-1'],key=157) 
  GeographicField23A = st.selectbox('select GeographicField23A:',['-1','25'],key=158)
  GeographicField24A = st.slider('select GeographicField24A:',-1,25,step =1)
  GeographicField25A = st.slider('select GeographicField25A:',-1,25,step =1)
  GeographicField26A = st.slider('select GeographicField26A:',-1,25,step =1)
  GeographicField28A = st.slider('select GeographicField28A:',-1,25,step =1)
  GeographicField29A = st.slider('select GeographicField29A:',-1,25,step =1)
  GeographicField30A = st.slider('select GeographicField30A:',-1,25,step =1)
  GeographicField30B = st.slider('select GeographicField30B:',-1,25,step =1)
  GeographicField31A = st.slider('select GeographicField31A:',-1,25,step =1)
  GeographicField32A = st.slider('select GeographicField32A:',-1,25,step =1)
  GeographicField33A = st.slider('select GeographicField33A:',-1,25,step =1)
  GeographicField34A = st.slider('select GeographicField34A:',-1,25,step =1)
  GeographicField35A = st.slider('select GeographicField35A:',-1,25,step =1)
  GeographicField36A = st.slider('select GeographicField36A:',-1,25,step =1)
  GeographicField37A = st.slider('select GeographicField37A:',-1,25,step =1)
  GeographicField37B = st.slider('select GeographicField37B:',-1,25,step =1)
  GeographicField38A = st.slider('select GeographicField38A:',-1,25,step =1)
  GeographicField39A = st.slider('select GeographicField39A:',-1,25,step =1)
  GeographicField40A = st.slider('select GeographicField40A:',-1,25,step =1)
  GeographicField41A = st.slider('select GeographicField41A:',-1,25,step =1)
  GeographicField42A = st.slider('select GeographicField42A:',-1,25,step =1)
  GeographicField43A = st.slider('select GeographicField43A:',-1,25,step =1)
  GeographicField44A = st.slider('select GeographicField44A:',-1,25,step =1)
  GeographicField45A = st.slider('select GeographicField45A:',-1,25,step =1)
  GeographicField46A = st.slider('select GeographicField46A:',-1,25,step =1)
  GeographicField47A = st.slider('select GeographicField47A:',-1,25,step =1)
  GeographicField47B = st.slider('select GeographicField47B:',-1,25,step =1)
  GeographicField49A = st.slider('select GeographicField49A:',-1,25,step =1)
  GeographicField50A = st.slider('select GeographicField50A:',-1,25,step =1)
  GeographicField51A = st.slider('select GeographicField51A:',-1,25,step =1)
  GeographicField53A = st.slider('select GeographicField53A:',-1,25,step =1)
  GeographicField54A = st.slider('select GeographicField54A:',-1,25,step =1)
  GeographicField55A = st.slider('select GeographicField55A:',-1,25,step =1)
  GeographicField56A = st.selectbox('select GeographicField56A:',['-1','25'],key=191)
  GeographicField56B = st.slider('select GeographicField56B:',-1,25,step =1)
  GeographicField57A = st.slider('select GeographicField57A:',-1,25,step =1)
  GeographicField58A = st.slider('select GeographicField58A:',-1,25,step =1)
  GeographicField59A = st.slider('select GeographicField59A:',-1,25,step =1)
  GeographicField60A = st.selectbox('select GeographicField60A:',['-1','25'],key=196)
  GeographicField60B = st.selectbox('select GeographicField60B:',['-1','25'],key=197)
  GeographicField61A = st.selectbox('select GeographicField61A:',['-1','25'],key=198)
  GeographicField61B = st.selectbox('select GeographicField61B:',['-1','25'],key=199)
  GeographicField62A = st.selectbox('select GeographicField62A:',['-1','25'],key=200)
  GeographicField62B = st.selectbox('select GeographicField62B:',['8','11','17','23','13','16','25','21','15','19','20','24','9','22','18','10','12','14','-1'],key=201)
  GeographicField63 = st.selectbox('select GeographicField63:',['Y','N',' '],key=202)
  GeographicField64 = st.selectbox('select GeographicField64:',['CA','NJ','TX','IL'],key=203)
  Year = st.selectbox('select year:', ['2013','2014','2015'],key=204)
  Month= st.selectbox('select Month:' ['1','2','3','4','5','6','7','8','9','10','11','12'],key=205)
  Weekday =st.selectbox('select weekday:' ['0','1','2','3','4','5','6'],key=206)
  Quarter = st.selectbox('select Quarter:',['1','2','3','4'], key=207)

  if st.button('Test Result'):
     acceptance= predict_result([
 'QuoteNumber',
 'QuoteConversion_Flag',
 'Field6',
 'Field7',
 'Field8',
 'Field9',
 'Field10',
 'Field11',
 'Field12',
 'CoverageField1A',
 'CoverageField5A',
 'CoverageField5B',
 'CoverageField6A',
 'CoverageField6B',
 'CoverageField8',
 'CoverageField9',
 'CoverageField11A',
 'SalesField1A',
 'SalesField1B',
 'SalesField2A',
 'SalesField2B',
 'SalesField3',
 'SalesField4',
 'SalesField5',
 'SalesField6',
 'SalesField7',
 'SalesField8',
 'SalesField9',
 'SalesField10',
 'SalesField11',
 'SalesField13',
 'SalesField14',
 'PersonalField1',
 'PersonalField4A',
 'PersonalField5',
 'PersonalField6',
 'PersonalField7',
 'PersonalField8',
 'PersonalField9',
 'PersonalField10A',
 'PersonalField11',
 'PersonalField12',
 'PersonalField13',
 'PersonalField14',
 'PersonalField15',
 'PersonalField16',
 'PersonalField17',
 'PersonalField18',
 'PersonalField19',
 'PersonalField22',
 'PersonalField27',
 'PersonalField28',
 'PersonalField29',
 'PersonalField30',
 'PersonalField31',
 'PersonalField34',
 'PersonalField39',
 'PersonalField40',
 'PersonalField49',
 'PersonalField54',
 'PersonalField59',
 'PersonalField64',
 'PersonalField65',
 'PersonalField66',
 'PersonalField67',
 'PersonalField69',
 'PersonalField70',
 'PersonalField74',
 'PersonalField79',
 'PersonalField84',
 'PropertyField1A',
 'PropertyField2A',
 'PropertyField2B',
 'PropertyField3',
 'PropertyField4',
 'PropertyField5',
 'PropertyField6',
 'PropertyField7',
 'PropertyField8',
 'PropertyField9',
 'PropertyField10',
 'PropertyField11A',
 'PropertyField11B',
 'PropertyField12',
 'PropertyField13',
 'PropertyField14',
 'PropertyField15',
 'PropertyField16A',
 'PropertyField17',
 'PropertyField18',
 'PropertyField19',
 'PropertyField20',
 'PropertyField21A',
 'PropertyField22',
 'PropertyField23',
 'PropertyField24A',
 'PropertyField25',
 'PropertyField26A',
 'PropertyField27',
 'PropertyField28',
 'PropertyField29',
 'PropertyField30',
 'PropertyField31',
 'PropertyField32',
 'PropertyField33',
 'PropertyField34',
 'PropertyField35',
 'PropertyField36',
 'PropertyField37',
 'PropertyField38',
 'PropertyField39A',
 'GeographicField1A',
 'GeographicField2A',
 'GeographicField3A',
 'GeographicField4A',
 'GeographicField5A',
 'GeographicField5B',
 'GeographicField6A',
 'GeographicField6B',
 'GeographicField7A',
 'GeographicField10A',
 'GeographicField10B',
 'GeographicField14A',
 'GeographicField17A',
 'GeographicField18A',
 'GeographicField18B',
 'GeographicField19A',
 'GeographicField20A',
 'GeographicField20B',
 'GeographicField21A',
 'GeographicField21B',
 'GeographicField22A',
 'GeographicField22B',
 'GeographicField23A',
 'GeographicField24A',
 'GeographicField25A',
 'GeographicField26A',
 'GeographicField28A',
 'GeographicField29A',
 'GeographicField30A',
 'GeographicField30B',
 'GeographicField31A',
 'GeographicField32A',
 'GeographicField33A',
 'GeographicField34A',
 'GeographicField35A',
 'GeographicField36A',
 'GeographicField37A',
 'GeographicField37B',
 'GeographicField38A',
 'GeographicField39A',
 'GeographicField40A',
 'GeographicField41A',
 'GeographicField42A',
 'GeographicField43A',
 'GeographicField44A',
 'GeographicField45A',
 'GeographicField46A',
 'GeographicField47A',
 'GeographicField47B',
 'GeographicField49A',
 'GeographicField50A',
 'GeographicField51A',
 'GeographicField53A',
 'GeographicField54A',
 'GeographicField55A',
 'GeographicField56A',
 'GeographicField56B',
 'GeographicField57A',
 'GeographicField58A',
 'GeographicField59A',
 'GeographicField60A',
 'GeographicField60B',
 'GeographicField61A',
 'GeographicField61B',
 'GeographicField62A',
 'GeographicField62B',
 'GeographicField63',
 'GeographicField64',
 'Year',
 'Month',
 'weekday',
 'Quarter'])
  st.success(acceptance)
if __name__ == '__main__':
  main()

  



  

  
 
