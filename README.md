# RouteGrader

Rock climbing is an increasingly popular sport that helps you stay in shape and make new friends. It’s an exciting activity for seasoned climbers, but like any sport it can be difficult for new climbers to get started. 

That’s where RouteGrader can help!

![dataframe preview](/figures/preview.png)

Climbing gyms have standardized interactive training walls called Moonboards. The online Moonboard community has collected and graded thousands of routes that can be configured at your local gym. Using RouteGrader, you can design your own custom route and have it graded on the spot! 

RouteGrader is a great tool to help new climbers get started with their Moonboard training, but it’s also useful for veteran climbers too. 

Do you have a favorite route that you’d like to make more difficult? Load it and tweak it in RouteGrader to see how much harder it is! If you’re stuck on a challenging route and want to make it easier, change a hold to give yourself a stepping stone on your way to the top. 

RouteGrader leverages the muscle of the Moonboard community and machine learning. Here’s how it works:

We first scrape the Moonboard community website for pre-graded routes. Each route contain information about where holds are located on the route and the difficulty of the route. This pre-graded route data is then stored in a database. 

Next, we use this data to train a custom machine learning model which can predict the difficulty of a previously unobserved route. 

Whether you’re new to the community or just looking to tune your climbing training, RouteGrader is the tool for you. 

## How it Works
### Web scraping and Data Collection
Web scraping and data collection are performed in the `webscraping/scratch.ipynb` notebook. We use `Requests` to first log into a Moonboard dashboard. Next, we save webpage snapshots containing links to all available bouldering routes. Using `BeautifulSoup` we can then scrape the snapshots for URLs pointing to each route. Finally, we can use `Requests` and `BeautifulSoup` together to scrape the HTML of the route's link for the holds present in the route. 

### Machine Learning
Machine learning is described in the `linear_model/linearmodel.ipynb` notebook. Holds have been parsed into a `pd.DataFrame` object which contains a list of the holds, their grades, the year the route was recorded, and the Moonboard angle of inclination:

![dataframe preview](/figures/dataframe_preview.png)

Most of the routes have an inclination of 40 degrees, so I discard routes that do not have this inclination. 

The routes are approximately normally distributed about a grade of 7A which may bias the predictions. I have not addressed this bias in the current version of the model. 

![dataframe preview](/figures/grade_distribution.png)

#### Encoding Holds
I encoded the holds by mapping the list of holds to a dictionary with indicator variables. For example, if the route had holds `[A1, B2]`
the dictionary is of the form `{'A1' : 1, 'B2': 1}`. I do not incorporate the type of hold (starting hold, intermediate hold, final hold) for encoding. 

Next, I used `DictVectorizer` from `scikit-learn` to embed the dictionary into feature space. The feature space is 198 dimensional and over $Z_2$ (indicator variables for each hold in a Moonboard). 

#### Model Selection
The `linear_model.ipynb` describes my model selection between ridge regression, an ensemble model (ridge regression + random forest), and a gradient boosted method (XGBoost). I found each model had approximatley the same $R^2$ score of 0.5, so I selected the linear model for quick training, serialization, and simplicity. 

I used `GridSearchCV` to tune the hyperparameter $\alpha$ for the `Ridge` regression model from `scikit-learn`. I found $\alpha$ was between 4 and 5. 

![dataframe preview](/figures/hyper_parameter_tuning.png)

Fine tuning saturated performance in this range, so I used $\alpha = 4$. 

### Frontend
After training my model, I serialized it using `pickle`. I built the frontend app using `Streamlit`. I had to modify some classes to deal with inverse transforming the model prediction, and these are done in `frontend/linear_model.py`. 