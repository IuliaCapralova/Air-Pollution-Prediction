# ml_industrty
Repository for the Machine Learning in Industry Practical


The basic structure of the repository is as follows, from the root folder:

- **data/**: Folder with the datasets.
    - **raw/**: Folder with the raw data.
    - **processed/**: Folder with the processed data.

- **src/**: Folder with the code.
    - **data/**: Folder with the data pipeline.
    - **features/**: Folder with the feature engineering pipeline.
    - **models/**: Folder with the models.
    - **utils/**: Folder with utility functions.

- **notebooks/**: Folder with the Jupyter notebooks.

- **results/**: Folder with the results.

- **tests/**: Folder with the tests.

- **deployment/**: Folder with the deployment code.

- **logs/**: Folder with the logs.

- **config/**: Folder with the configuration files.

- **README.md**: File with instructions.

- **env/**: Python environment for the project. Activate with ```conda activate env/``` or ```pip install -r requirements``` to install it manually.

- **requirements.txt**: File with the dependencies.


## CODE INSTRUCTIONS

# Data preprocessing (not needed at this step)
The data preprocessing can be run from src/data/main.py. It reads the datasets
from data/raw and inserts the processed data into data/processed. The feature
engineering is (for now) run from src/features/feature_eng.py which loads the
preprocessed datasets and saves the pca transformed data into data/processed.

# Model training and data preparation for the dashboard
Running "python -m src.models.main" trains 6 different models (O3 and NO2
linear regressor, O3 and NO2 LSTM, O3 and NO2 MLP). It saves all the data
shown in the dashboard under "results". The number of time steps to predict
can be specified under "n_steps_predict", and the month to predict under
"month". The data under results currently shows the model's predictions for
April. The dashboard is run via "streamlit run src/utils/dashboard.py".
