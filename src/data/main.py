import pandas as pd
from dataset_loader import DataSetLoader
from meteo_dataset import MeteoDataset
from pollutant_dataset import PollutantDataset

def main():
    loader = DataSetLoader()

    O3_dataset = PollutantDataset(variable="O3")
    # print(len(O3_dataset))
    # print(O3_dataset[3])
    df_O3 = O3_dataset.get_df()
    # print(df_O3.head())
    loader(O3_dataset, "data/processed/O3.csv")

    NO2_dataset = PollutantDataset(variable="NO2")
    # print(len(NO2_dataset))
    # print(NO2_dataset[3])
    df_NO2 = NO2_dataset.get_df()
    # print(df_NO2.head())
    loader(NO2_dataset, "data/processed/NO2.csv")

    meteo_dataset = MeteoDataset(variable="meteo")
    # print(len(meteo_dataset))
    # print(meteo_dataset[3])
    df_meteo = meteo_dataset.get_df()
    # print(df_meteo.head())
    loader(meteo_dataset, "data/processed/meteo.csv")

    combined = pd.concat([df_meteo, df_NO2[['NO2']], df_O3[['O3']]], axis=1)
    print(combined.head(10))
    print(combined.isnull().sum())
    loader(combined, "data/processed/combined.csv")



if __name__ == "__main__":
    main()
