import pandas as pd

updated_cleaned_properties_path = './data/curated/cleaned_all_properties1.csv'

updated_cleaned_properties_df = pd.read_csv(updated_cleaned_properties_path)

def split_hyphenated_districts(df):

    df_split = df['District'].str.split('-', expand=True).stack().reset_index(level=1, drop=True)
    df_split.name = 'District' 

    df_expanded = df.drop(columns=['District']).join(df_split)
    
    return df_expanded

expanded_cleaned_properties_df = split_hyphenated_districts(updated_cleaned_properties_df)

expanded_cleaned_properties_df = expanded_cleaned_properties_df[~expanded_cleaned_properties_df['District'].str.contains('Group Total', case=False, na=False)]

output_file_path = './data/curated/expanded_cleaned_properties.csv'
expanded_cleaned_properties_df.to_csv(output_file_path, index=False)

output_file_path
