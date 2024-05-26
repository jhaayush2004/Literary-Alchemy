def hybrid_recommender(book_already_read, user_id, weight_for_history):
    import random
    
    def book_recommendations_UserBased_CF(user_id):
            try:
                serial_no=book_pivotub.index.get_loc(user_id)
                
            except KeyError:
                print("Sorry! UserID",user_id,"not Valid.")
                
            distance,suggestions=modelub.kneighbors(book_pivotub.loc[user_id].values.reshape(1,-1), n_neighbors=6)
            h=[]
            for i in suggestions:
                h.append(book_pivotub.index[i])
            y=[h[0][1],h[0][2],h[0][3],h[0][4],h[0][5]]
            z=[]
            for i in y:
                max_value = book_pivotub.loc[i].max()  
                max_indices = book_pivotub.loc[i][book_pivotub.loc[i] == max_value].index.tolist()  
                max_index = random.choice(max_indices)
                z.append(max_index)
            z=np.array(z)
            z=z.flatten()
            return z
    def recommend_book_itemBased_CF(book_already_read):
            book_id=np.where(book_pivotib.index==book_already_read)[0][0]
            distance,suggestions=modelib.kneighbors(book_pivotib.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)
            x=np.array(suggestions)
            x=x.flatten()
            y=[]
            for i in x:
                y.append(book_pivotib.index[i])
            y=np.array(y)
            y=y.flatten()
            return y
    z=book_recommendations_UserBased_CF(user_id)
    y=recommend_book_itemBased_CF(book_already_read)
    k=int(np.floor(weight_for_history*len(y)))
    m=random.sample(y.tolist(),k)
    for i in range(len(z)-k):
        m.append(z[i])
    print("Hybrid Recommendations\n")
    for i in m:
        print(i)    
