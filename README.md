# Movie Recommendation System using NetworkX and Clustering

This project implements a Movie Recommendation System using NetworkX library for graph-based similarity analysis, clustering techniques, and cosine similarity for content-based recommendations. The system provides personalized movie recommendations based on user input and similarity between movies.

## Project Overview

The Movie Recommendation System is designed to offer movie suggestions to users based on their input movie. It uses a combination of NetworkX, clustering, and cosine similarity to identify similar movies and provide relevant recommendations.

## Features

- User Interface: The frontend is developed using HTML, CSS, and JavaScript to take input movie from the user and display the recommended movies.
- Backend: The system's backend is powered by Django, which handles user requests, processes data, and provides responses.
- Graph-based Similarity: NetworkX library is used to construct a graph of movies based on their similarity, enabling efficient similarity analysis.
- Clustering: MiniBatchKMeans clustering is employed to group similar movies together, improving recommendation accuracy.
- Cosine Similarity: TF-IDF vectorization and cosine similarity are used for content-based recommendations, considering movie descriptions.
- Kaggle Dataset: The movie dataset is sourced from Kaggle, containing movie details such as title, director, cast, genre, description, etc.

## How to Use

1. Clone the repository: `git clone https://github.com/yourusername/movierecommendation.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Django server: `python manage.py runserver`
4. Access the system from your browser: `http://localhost:8000`

## Project Structure

- `data/`: Contains the movie dataset obtained from Kaggle.
- `frontend/`: Holds the HTML, CSS, and JavaScript files for the user interface.
- `backend/`: Includes the Django backend files for handling user requests and processing data.
- `recommendation/`: Contains the core recommendation code using NetworkX, clustering, and cosine similarity.

## Future Enhancements

1. Implement user authentication to provide personalized recommendations.
2. Incorporate user feedback to continuously improve the recommendation system.
3. Expand the movie dataset to include more recent movies and diverse genres.
4. Explore other similarity measures and algorithms to enhance recommendation accuracy.

## Credits

- Kaggle Dataset: [Kaggle Movies Dataset](https://www.kaggle.com/usernam3/moviedataset)

---
Your Name (mohdfaizansaifi000@gmail.com)
