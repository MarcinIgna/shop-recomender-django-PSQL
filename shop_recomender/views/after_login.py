from django.shortcuts import render, get_object_or_404
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from shop_recomender.models.user import User
from shop_recomender.models.order import Order
from shop_recomender.models.product import Product
import matplotlib.pyplot as plt

def after_login(request):
    user_id = request.session.get('my_user_id')
    print("User ID in after login:", user_id)
    user = get_object_or_404(User, id=user_id)

    if user.is_admin:
        return render(request, 'admin/admin_home.html', {'user': user})
    else:
        # Retrieve user's recent purchases
        recent_purchases = Order.objects.filter(user=user).order_by('-order_date')[:3]

        # Get recommendations based on user's purchases
        recommendations = get_recommendations(user)
        
        if recommendations is None:
            recommendations = []  # Handle None case

        return render(request, 'user/main_home.html', {'user': user, 'purchases': recent_purchases, 'recommendations': recommendations})


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(user):
    # Retrieve user's purchases
    user_purchases = Order.objects.filter(user=user)
    product_ids = [purchase.product.id for purchase in user_purchases]

    # Retrieve product descriptions for user's purchases
    product_descriptions = Product.objects.filter(id__in=product_ids).values_list('description', flat=True)

    print("Product Descriptions:", product_descriptions)

    if not product_descriptions:
        # Handle the case when there are no product descriptions available
        print("No product descriptions available.")
        return None

    # Perform TF-IDF vectorization on product descriptions
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(product_descriptions).toarray()

    print("TF-IDF Matrix Shape:", tfidf_matrix.shape)

    # Visualize the TF-IDF values for a specific product
    product_index = 0  # Index of the product in the TF-IDF matrix
    tfidf_values = tfidf_matrix[product_index]

    # Plot a bar chart of the TF-IDF values
    plt.bar(range(len(tfidf_values)), tfidf_values)
    plt.xlabel('Feature Index')
    plt.ylabel('TF-IDF Value')
    plt.title('TF-IDF Values for Product')
    # Save the figure as an image file
    plt.savefig('tfidf_plot.png')

    # Calculate similarity between user profile and all products
    user_profile = tfidf_matrix.mean(axis=0)
    similarities = cosine_similarity(user_profile.reshape(1, -1), tfidf_matrix)

    # Get top-N most similar products
    top_n = 3  # Adjust as needed
    similar_product_indices = similarities.argsort()[0][-top_n:][::-1]
    similar_products = Product.objects.filter(id__in=similar_product_indices)

    return similar_products

# def get_recommendations(user):
#     # Retrieve user's purchases
#     user_purchases = Order.objects.filter(user=user)
#     product_ids = [purchase.product.id for purchase in user_purchases]

#     # Retrieve product descriptions for user's purchases
#     product_descriptions = Product.objects.filter(id__in=product_ids).values_list('description', flat=True)

#     print("Product Descriptions:", product_descriptions)

#     # Perform TF-IDF vectorization on product descriptions
#     tfidf_vectorizer = TfidfVectorizer()
#     tfidf_matrix = tfidf_vectorizer.fit_transform(product_descriptions).toarray()

#     print("TF-IDF Matrix Shape:", tfidf_matrix.shape)
    
#     # Visualize the TF-IDF values for a specific product
#     product_index = 0  # Index of the product in the TF-IDF matrix
#     tfidf_values = tfidf_matrix[product_index]

#     # Plot a bar chart of the TF-IDF values
#     plt.bar(range(len(tfidf_values)), tfidf_values)
#     plt.xlabel('Feature Index')
#     plt.ylabel('TF-IDF Value')
#     plt.title('TF-IDF Values for Product')
#     # Save the figure as an image file
#     plt.savefig('tfidf_plot.png')

#     # Calculate similarity between user profile and all products
#     user_profile = tfidf_matrix.mean(axis=0)
#     similarities = cosine_similarity(user_profile.reshape(1, -1), tfidf_matrix)

#     # Get top-N most similar products
#     top_n = 3  # Adjust as needed
#     similar_product_indices = similarities.argsort()[0][-top_n:][::-1]
#     similar_products = Product.objects.filter(id__in=similar_product_indices)

#     return similar_products






