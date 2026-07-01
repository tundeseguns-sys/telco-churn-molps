import pandas as pd

from mlops_tutorial.config import INGESTION_REPORT_FILE, RAW_DATA_FILE


def check_raw_exists() -> None:
    '''
    Check that the raw data file exist.
    This function does not modify the raw file
    '''

    if not RAW_DATA_FILE.exists():
        raise FileNotFoundError(
            "Raw data file not found: (RAW_DATA_FILE)\n"
            "Please place the raw CSV inside data/raw/ "
            "and name it Telco-Customer-Churn.csv"
        )


def load_raw_data() -> pd.DataFrame:
    """
    load the raw CSV file.
    The file is read only. It is not changed.
    """

    check_raw_exists()

    dataframe = pd.read_csv(RAW_DATA_FILE)

    return dataframe


def create_ingestion_report(dataframe: pd.DataFrame) -> None:
    '''
    Create a simple ingestion report.

    This report confirms that the raw data was loaded.
    Detailed inspection and EDA will happen in later.
    '''

    INGESTION_REPORT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    report_text = f"""
DATA INGESTION REPORT
======================

Raw data file:
{RAW_DATA_FILE}

File exists:
{RAW_DATA_FILE.exists()}

Number of rows:
{dataframe.shape[0]}

Number of columns:
{dataframe.shape[1]}

column names:
{dataframe.columns.tolist()}
"""

    INGESTION_REPORT_FILE.write_text(
        report_text,
        encoding="utf-8",
    )


def run_data_ingestion() -> pd.DataFrame:
    '''
    Run data ingestion process.
    '''

    dataframe = load_raw_data()

    create_ingestion_report(dataframe)

    print("Data ingestion complited succesfully.")
    print(f"Rows: {dataframe.shape[0]}")
    print(f"Columns: {dataframe.shape[1]}")
    print(f"Report saved to: {INGESTION_REPORT_FILE}")

    return dataframe


if __name__ == "__main__":
    run_data_ingestion()
