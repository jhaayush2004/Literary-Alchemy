ratings['user_id'].value_counts().shape
#We would consider only those user who has read and commented/rated 175+ books.This would help us to get best knowledge about books.
desired_users=ratings['user_id'].value_counts()>175
desired_users=desired_users[desired_users]
x=desired_users.index
ratings=ratings[ratings['user_id'].isin(x)]
ratings_plus_book=ratings.merge(books, on='ISBN')
ratings_plus_book.groupby('title')['rating'].count()
rating_count=ratings_plus_book.groupby('title')['rating'].count().reset_index()
rating_count.rename(columns={'rating':'number_of_ratings'}, inplace=True)
ratings_plus_book=ratings_plus_book.merge(rating_count, on='title')
#We would consider only those books which are read/rated by 75+ users on the platform.
ratings_plus_book['number_of_ratings']>75
ratings_plus_book=ratings_plus_book[ratings_plus_book['number_of_ratings']>75]
