book_pivotib=ratings_plus_book.pivot_table(columns='user_id',index='title',values='rating')
book_pivotib.fillna(0,inplace=True)
from scipy.sparse import csr_matrix
sparse_ib=csr_matrix(book_pivotib)
from sklearn.neighbors import NearestNeighbors
modelib=NearestNeighbors(metric='minkowski',p=2,algorithm='brute')
#Its basically euclidean dis.(as p=2),its manhattan for p=1.
distances,suggestions=modelib.kneighbors(book_pivotib.iloc[...,:].values.reshape(1,-1),n_neighbors=6)
x=np.array(suggestions)
y=x.flatten()
def recommend_book_itemBased_CF(book_name):
    book_id=np.where(book_pivotib.index==book_name)[0][0]
    distance,suggestions=modelib.kneighbors(book_pivotib.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)
    x=np.array(suggestions)
    x=x.flatten()
    for i in x:
        print(book_pivotib.index[i])
