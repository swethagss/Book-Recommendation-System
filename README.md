# Book Recommendation System

This project implements a Book Recommendation System using a collaborative filtering approach with the Nearest Neighbors (NN) algorithm. The system recommends books based on user interactions, specifically by finding similarities between books in a user-item matrix. Given a book that a user likes, the system suggests other books that are similar, based on historical user preferences.

## Table of Contents
- [Overview](#overview)
- [Types of Recommendation Systems](#types-of-recommendation-systems)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Features](#features)
- [Model and Data Artifacts](#model-and-data-artifacts)
- [Model Evaluation](#model-evaluation)
- [Deployment](#deployment)
- [Future Work](#future-work)

## Overview

Recommendation systems play a crucial role in simplifying decision-making for users in today's fast-paced world. They provide personalized content suggestions by analyzing user preferences, browsing history, and similar users' actions.
Recommendation systems utilize advanced Artificial Intelligence algorithms to curate customized content lists. These systems save time and cognitive resources by filtering relevant items for users based on their interests and behaviors.

## Types of Recommendation Systems

### 1. Content-Based

  **Definition**:  
  Content-based recommendation systems focus on the attributes of items (such as books, movies, or music) and user preferences. They suggest items similar to those a user has previously interacted with, based on the features of the items themselves.

  **Examples**:  
  - Twitter: Recommends tweets based on the content you engage with.  
  - YouTube: Suggests videos similar to the ones you've watched.

  **Features Considered**:  
  - Characteristics of the item (e.g., genre, description, author).  
  - User behavior, such as:  
  - What music you are listening to.  
  - What singer or artist you are watching.  
  - Embedded features like keywords or topics.
 
  **Mechanism**:  
  - A vector of item features is created for each item.  
  - The system compares the feature vector of the user's preferred items with other items to find matches.  
  - The hypothesis is that if a user liked an item before, they are likely to enjoy similar items in the future.

  **Challenges**:  
  - **Over-specialization**: Recommends very similar items, leading to a lack of diversity in suggestions.  
  - **Cold-Start Problem**: Struggles to make recommendations for new users or items with limited data.

---
### 2. Collaborative Filtering

  **Definition**:  
  Collaborative filtering systems analyze the user-item interaction history to identify patterns of similarity between users or items. They recommend items based on the behavior of other users with similar preferences.

  **Examples**:  
  - Netflix: Recommends shows based on viewing habits of users with similar preferences.  
  - Amazon: Suggests products based on the purchases of users with similar buying patterns.

  **Mechanism**:  
  - Clusters users or items with similar preferences.  
  - Two main approaches:  
  1. **User-User Collaborative Filtering**: Finds users with similar interaction histories and suggests items liked by those users.  
  2. **Item-Item Collaborative Filtering**: Identifies items similar to those a user has interacted with and recommends them.  

  **Challenges**:  
  - **Data Sparsity**: Interaction matrices often have many missing values.  
  - **Cold-Start Problem**: Difficulty recommending items for new users or new products.  
  - **Popularity Bias**: Tends to recommend popular items, neglecting niche options.

---

### 3. Hybrid Systems
  **Definition**:  
Hybrid systems combine two or more recommendation approaches, such as content-based and collaborative filtering, to leverage the strengths of each method and overcome their weaknesses.

  **Examples**:  
  - Netflix: Uses both content-based and collaborative filtering methods to provide recommendations.  
  - Spotify: Combines collaborative filtering with deep learning techniques for personalized music recommendations.

  **Mechanism**:  
  - Incorporates multiple models:  
  - Content-based filtering for analyzing item features.  
  - Collaborative filtering for user interaction patterns.  
  - Advanced techniques like embeddings (e.g., word2vec) to encode relationships.  
  - Combines results from different models to improve recommendation accuracy.

  **Challenges**:  
  - **Computational Complexity**: Increases due to the integration of multiple algorithms.  
  - **Balancing Approaches**: Requires careful tuning to avoid over-reliance on one method.  
  - **Scalability**: Managing large datasets for multiple algorithms can be resource-intensive.

---

### 4. Knowledge-Based Systems

**Definition**:  
Knowledge-based systems recommend items based on explicit user preferences or rules derived from domain knowledge.

**Examples**:  
- Travel websites: Recommend destinations based on user-specified preferences like budget, activities, or climate.  
- Car selection tools: Suggest cars based on user-input criteria such as mileage, price, and brand.

**Mechanism**:  
- Uses explicit user input (e.g., filters, preferences).  
- Applies rules or domain-specific knowledge to find suitable matches.  

**Challenges**:  
- **User Input Dependency**: Requires users to provide detailed preferences.  
- **Knowledge Maintenance**: Rules must be updated regularly to reflect changes in the domain.  
- **Cold-Start Problem**: Limited ability to generalize across users without prior knowledge.

---

### 5. Context-Aware Systems

**Definition**:  
Context-aware systems factor in contextual information, such as time, location, or device type, to enhance recommendations.

**Examples**:  
- Uber Eats: Suggests restaurants based on time of day and location.  
- Google Maps: Recommends places to visit based on current location and time.

**Mechanism**:  
- Contextual features (e.g., time, weather, user activity) are integrated into the recommendation process.  
- Adapts recommendations dynamically based on changing contexts.  

**Challenges**:  
- **Data Collection**: Requires extensive contextual data, which may raise privacy concerns.  
- **Complex Modeling**: Integrating contextual features increases model complexity.  
- **Scalability**: Managing and processing context data at scale is challenging.

## Dataset

The dataset includes a user-book interaction matrix that records user ratings for various books. This matrix is transformed into a format suitable for the NN algorithm to identify similarities effectively.

## Data Preprocessing

Key preprocessing steps:
- **Loading the Data**: Handling missing or inconsistent values.
- **User-Item Matrix Creation**: Rows represent users, columns represent books, and entries indicate user ratings.
- **Filling Missing Values**: Ensuring completeness for effective model training.
- **EDA**: Visualizing feature distributions.

## Features

- **User-Book Interaction Analysis**: Creates a matrix of user ratings for books.
- **Nearest Neighbors Model**: Trains a KNN model to identify book similarities.
- **Book Recommendation**: Suggests books based on user preferences.
- **Model Persistence**: Saves trained models for efficient reuse.

## Model and Data Artifacts

### Model
- **Nearest Neighbors (KNN)**: This recommendation system uses a K-Nearest Neighbors (KNN) model to identify and recommend books similar to a user-specified book. The model calculates similarities between books based on user ratings and suggests the closest matches.

### Artifacts
- `model.pkl`: Trained KNN model.
- `book_names.pkl`: Maps book IDs to titles.
- `final_rating.pkl`: Preprocessed user-item matrix.
- `book_pivot.pkl`: Optimized pivoted matrix for similarity calculations.

## Model Evaluation
The effectiveness of the Nearest Neighbors (KNN) model is evaluated through qualitative assessment based on the relevance of the recommended books. After executing the recommendation function, the model provides a list of books similar to the user-specified input.

### Qualitative Evaluation
- **Relevance**: The recommended books are qualitatively checked for relevance to the input book. For example, recommending books from the same series (e.g., other "Harry Potter" books when the input is a "Harry Potter" title) indicates that the model is correctly identifying similar items.
- **User Experience**: The system's ability to avoid recommending the same book that the user searched for (as implemented in the function) enhances the user experience by providing diverse recommendations.

## Deployment
The model is deployed via a Streamlit app, allowing users to select a book and view recommendations. Run the app using the following link:

[Book Recommendation System app](https://swethagss-book-recommendation-system-app1-xwq8ow.streamlit.app)

## Future Work

- **Additional Features**: Include book genres, authors, and user demographics.
- **Quantitative Metrics**: Incorporate precision, recall, and F1 score.
- **Algorithm Exploration**: Test advanced models like deep learning or matrix factorization.
- **Enhanced User Interface**: Develop a web or mobile app.
- **Cold-Start Problem**: Address new user/item recommendation challenges.


