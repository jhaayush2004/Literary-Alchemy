users=pd.read_csv(r"C:\Users\Ayush\Downloads\Users.csv",error_bad_lines=False,encoding='latin-1')
users.rename(columns={'User-ID':'user_id','Location':'location','Age':'age'}, inplace=True)
users['age'].isna().sum()
users['age'].fillna(0, inplace=True)
