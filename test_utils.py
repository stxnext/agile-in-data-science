import pandas as pd

from utils import explode_str_column


def test_explode_str_column():
    input_df = pd.DataFrame(
        {
            "a": [1, 2],
            "b": ["foo;bar", "spam;ham;eggs"]
        }
    )
    column_to_explode = "b"
    expected_df = pd.DataFrame(
        {
            "a": [1, 1, 2, 2, 2],
            "b": ["foo", "bar", "spam", "ham", "eggs"]
        },
        index=[0, 0, 1, 1, 1]
    )
    actual_df = explode_str_column(input_df, column_to_explode)
    pd.testing.assert_frame_equal(actual_df, expected_df)
