import pandas as pd

def data_prep(encoder, **kwargs):
    input_cols = ['Levy','Prod. year', 'Category', 'Leather interior', 
                  'Fuel type', 'Engine volume', 'Mileage', 'Cylinders', 
                  'Gear box type', 'Drive wheels', 'Airbags', 'Turbo']

    data_dict = {
        'Levy': kwargs.get('levy'),
        'Prod. year': kwargs.get('year'),
        'Category': kwargs.get('cat'),
        'Leather interior': kwargs.get('li'),
        'Fuel type': kwargs.get('fuel'),
        'Engine volume': kwargs.get('ev'),
        'Mileage': kwargs.get('mileage'),
        'Cylinders': kwargs.get('cylinders'),
        'Gear box type': kwargs.get('gear'),
        'Drive wheels': kwargs.get('wheel'),
        'Airbags': kwargs.get('airbags'),
        'Turbo': kwargs.get('turbo')
    }
    raw_df = pd.DataFrame([data_dict])

    numerical_cols = raw_df.select_dtypes(include=['int', 'float']).columns.to_list()
    cat_cols = raw_df.select_dtypes(include='object').columns.to_list()

    encoded_cols = list(encoder.get_feature_names_out(cat_cols))
    encoded_vals = encoder.transform(raw_df[cat_cols])

    encoded_df = pd.DataFrame(encoded_vals, columns=encoded_cols)

    df_final = pd.concat([raw_df[numerical_cols].reset_index(drop=True),
                          encoded_df.reset_index(drop=True)], axis=1)

    return df_final