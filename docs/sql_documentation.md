# SQL Documentation

## Schema Design
After pulling historical data with yfinance, we created the `apple_crises_db` database in PostgreSQL with two main tables:
- `assets`: Stores asset metadata, using `ticker` as the primary key.
- `market_data`: Stores daily OHLCV records. It uses a composite primary key on (`trade_date`, `ticker`) to prevent duplicate daily records per stock, and references `assets(ticker)` as a foreign key. Numeric types were used for price columns to avoid overflow and maintain precision.

## Data Loading
Data was loaded into PostgreSQL from CSV files using psql's \copy command:
- `assets.csv` was loaded into the `assets` table.
- `market_data.csv` was loaded into the `market_data` table matching the column order: `trade_date`, `ticker`, `open`, `high`, `low`, `close`, `adj_close`, `volume`.

## Data Validation
We ran `data_validation.sql` to verify the dataset before analysis:
- Entity & Row Count Check: Verified all 4 assets (AAPL, QCOM, GLW, XLK) loaded properly, each having 794 trading rows covering the same date span.
- Missing Values: Checked that no null values exist across any price, date, or volume fields.
- Duplicate Detection: Confirmed there are no duplicate date and ticker pairs using GROUP BY with a HAVING count > 1 filter.
- Value Sanity: Checked that prices and volumes contain no negative values or zeros.
- Candlestick Logic: Checked that daily highs are greater than or equal to open, close, and low prices, and lows are less than or equal to open and close prices.
