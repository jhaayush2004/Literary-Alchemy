book_pivotub=ratings_plus_book.pivot_table(columns='title', index='user_id', values='rating')
book_pivotub.fillna(0, inplace=True)
from scipy.sparse import csr_matrix
sparse_ub=csr_matrix(book_pivotub)
from sklearn.neighbors import NearestNeighbors
modelub=NearestNeighbors(algorithm='brute',metric='minkowski',p=2)
modelub.fit(sparse_ub)
distance,suggestions=modelub.kneighbors(book_pivotub.iloc[....,:].values.reshape(1,-1),n_neighbors=6)
#Now we are able to find serial_no. of similar users from a given user_id.Now,our task is to figure out that which books are among the maximum rated books of these users and select a random such books for each users.
h=[]
for i in suggestions:
    h.append(book_pivotub.index[i])
h    
book_pivotub.loc[.....].idxmax()
y=[h[0][1],h[0][2],h[0][3],h[0][4],h[0][5]]
import random
for i in y:
    max_value = book_pivotub.loc[i].max()  
    max_indices = book_pivotub.loc[i][book_pivotub.loc[i] == max_value].index.tolist()  
    max_index = random.choice(max_indices)  
    print(max_index)
  serial=np.where(book_pivotub.index==.....)[0][0]
def book_recommendations_UserBased_CF(user_id):
    import random
    
    try:
        serial_no=book_pivotub.index.get_loc(user_id)
        #serial_no=np.where(book_pivotub.index==user_id)[0][0]
    except KeyError:
        print("Sorry! UserID",user_id,"not Valid.")
        
    distance,suggestions=modelub.kneighbors(book_pivotub.loc[user_id].values.reshape(1,-1), n_neighbors=6)
    # we could also use distance,suggestions=modelub.kneighbors(book_pivotub.iloc[serial_no].values.reshape(1,-1), n_neighbors=6)
    h=[]
    for i in suggestions:
        h.append(book_pivotub.index[i])
    y=[h[0][1],h[0][2],h[0][3],h[0][4],h[0][5]]
    
    for i in y:
        max_value = book_pivotub.loc[i].max()  
        max_indices = book_pivotub.loc[i][book_pivotub.loc[i] == max_value].index.tolist()  
        max_index = random.choice(max_indices)  
        print(max_index)
