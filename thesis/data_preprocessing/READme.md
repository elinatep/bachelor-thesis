# Data Preprocessing

## Flowchart

Generate_dataset -> 0labels_septicshock.txt -> pos_neg_extract.py (extract pos&neg patients) -> negative.csv / positive.csv -> data_merge.py (merge with vitals) -> negative_merged_data.csv / positive_merged_data.csv -> null_vitals.py (exclude patients with at least 1 empty column of vitals) -> filtered_negative_data.py / filtered_positive_data.py -> labelling.py (label data with 1&0) -> labeled_positive_database.csv / labeled_negative_database.csv -> missing.py (deal with missing values) -> labeled_positive_database.csv / labeled_negative_database.csv -> time_ref.py (calculate relative time from shock for pos. and from 1st vital for neg) -> labeled_positive_database.csv / labeled_negative_database.csv -> 30mins.py (resample data to 30min grid) -> neg_301.csv / pos_301.csv -> data_filter.ipynb (for each pos patient choose 4 neg patients and cut the LOS, check ranges of vitals) -> combined_data.py

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)