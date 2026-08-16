\echo 'Number of Assets'
select count(*) from assets;
select ticker from assets;

\echo ''
\echo 'Market Data Validation'
select count(*) from market_data;

\echo 'Check for NULLs across all fields'
select count(*) from market_data
where trade_date is null
   or open is null
   or high is null
   or low is null
   or close is null
   or adj_close is null
   or volume is null;

\echo 'Check for duplicates'
select trade_date, ticker, COUNT(*)
from market_data
group by trade_date, ticker
having count(*) > 1;

\echo 'Check coverage and counts per ticker'
select ticker, count(*), min(trade_date), max(trade_date)
from market_data
group by ticker;

\echo 'Check for negative values'
select count(*) from market_data
where volume < 0 or low < 0 or open < 0 or close < 0;

\echo 'Check OHLC candlestick integrity'
select count(*) from market_data
where high < open
   or high < close
   or low > open
   or low > close;
