# Get Government Data
This module posts the data from the [government data](https://fdc.nal.usda.gov/fdc-datasets) into the database.

The posting is controlled via the database schema, and file naming conventions.
`
## Running the script

The script accepts two environment variables:

`DATA_DIR` overrides the default location, 'data', for writing the data files from the government website.

`GOVT_DATA_URL` overrides the default government url, 'https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_csv_2019-12-17.zip', for the file download.
