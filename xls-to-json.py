from pathlib import Path
import argparse
import re

import pandas as pd

DATABASE_FILE = 'worldcup26.json'


def resolve_input_file() -> Path:
	parser = argparse.ArgumentParser(description='Convert a CSV/XLSX file to JSON and SQLite.')
	parser.add_argument('input_file', nargs='?', help='Input CSV or XLSX file path')
	args = parser.parse_args()

	if args.input_file:
		return Path(args.input_file)

	default_xlsx = Path(DATABASE_FILE.removesuffix('.json') + '.xlsx')
	if default_xlsx.exists():
		return default_xlsx

	raise FileNotFoundError('No input file found. Provide a CSV/XLSX path as an argument.')


def load_table(file_path: Path) -> pd.DataFrame:
	if file_path.suffix.lower() in {'.xlsx', '.xls'}:
		return pd.read_excel(file_path, sheet_name='Sheet1')
	raise ValueError(f'Unsupported file type: {file_path.suffix}')

INPUT_FILE = resolve_input_file()

df = load_table(INPUT_FILE)
if 'date' in df.columns:
	df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')


df.to_json(DATABASE_FILE, orient='records', force_ascii=False, indent=2)

print('Columns:', ', '.join(df.columns))
