import pandas as pd
import numpy as np
#extracting and manipulating books data
books=pd.read_csv(r"C:\Users\Ayush\Downloads\Books.csv",error_bad_lines=False,encoding='latin-1')
books.drop(['Image-URL-S','Image-URL-M','Image-URL-L'],axis=1,inplace=True)
books.rename(columns={'Book-Title':'title','Book-Author':'author','Year-Of-Publication':'year','Publisher':'publisher'}, inplace=True)
