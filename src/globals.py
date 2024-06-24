import preprocess

# Load and preprocess data
file_path = './assets/data/powerconsumption.csv'
df = preprocess.data_preprocess(file_path)
df_hourly = preprocess.get_HourlyData(df)
df_daily = preprocess.get_DailyData(df)