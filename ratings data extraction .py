ratings=pd.read_csv(r"C:\Users\Ayush\Downloads\Ratings.csv",error_bad_lines=False,encoding='latin-1')
ratings.rename(columns={'User-ID':'user_id','Book-Rating':'rating'}, inplace=True)
