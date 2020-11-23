def explode_str_column(df, column):
    df[column] = df[column].str.split(";")
    return df.explode(column)
