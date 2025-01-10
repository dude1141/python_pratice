import pandas
import pandas as pd
pd
<module 'pandas' from 'C:\\Users\\mouni\\Downloads\\pythoninstall\\lib\\site-packages\\pandas\\__init__.py'>
l2=[10,20,30,40]
pd.Series(l2)
0    10
1    20
2    30
3    40
dtype: int64


pd.Series(l2,index=["i","ii","iii","iiii"])
              
i       10
ii      20
iii     30
iiii    40
dtype: int64


pd.DataFrame(l2)
    0
0  10
1  20
2  30
3  40
l=[10,20,30]


s=pd.Series(l)
print(s)
0    10
1    20
2    30


                         
s=pd.Series(a)                        
print(s)           
0    1
1    2
2    4
3    5
dtype: int32

#pandas dataframe
#below is list of tuples
d=[("85","ECE"),("98","BCE")]
pd.DataFrame(d)                        
    0    1
0  85  ECE
1  98  BCE
