import matplotlib.pyplot as plt
import pandas as pd

# Function to plot and save all districts from one dataset
def plot_and_save_all_districts(predicted_rent_prices_df, dataset_name, save_path):
    plt.figure(figsize=(12, 8))
    
    for sa2_name in predicted_rent_prices_df['SA2_NAME'].unique():
        sa2_data = predicted_rent_prices_df[predicted_rent_prices_df['SA2_NAME'] == sa2_name].drop('SA2_NAME', axis=1).T
        sa2_data.index = pd.to_datetime(sa2_data.index)
        plt.plot(sa2_data.index, sa2_data.values, label=sa2_name)
    
    plt.xlabel('Date (Quarters)')
    plt.ylabel('Predicted Rent Price')
    plt.title(f'Predicted Rent Prices for All Districts - {dataset_name}')
    plt.xticks(rotation=45)
    plt.legend(title="SA2 Areas", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()

# Load the two CSV files
file_1_path = './models/predicted_rent_prices_2025_2027_optimized_ensemble.csv'
file_2_path = './models/predicted_rent_prices_2025_2027_optimized_ensemble_2.csv'

predicted_rent_prices_df_1 = pd.read_csv(file_1_path)
predicted_rent_prices_df_2 = pd.read_csv(file_2_path)

save_path_1 = './plots/predicted_rent_prices_dataset_1.png'
save_path_2 = './plots/predicted_rent_prices_dataset_2.png'

# Save the plots for both datasets to the specified paths
plot_and_save_all_districts(predicted_rent_prices_df_1, "Dataset 1", save_path_1)
plot_and_save_all_districts(predicted_rent_prices_df_2, "Dataset 2", save_path_2)

# Output file names where the plots are saved
print('Plots saved as: predicted_rent_prices_dataset_1.png and predicted_rent_prices_dataset_2.png')
