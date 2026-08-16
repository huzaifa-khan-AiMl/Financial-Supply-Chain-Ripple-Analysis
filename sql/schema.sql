\echo 'Assets Table made'
create table assets (
    ticker varchar(20) primary key,
    company_name varchar(100),
    sector varchar(100),
    role varchar(100)
);

\echo ''
\echo 'Market Data Table made'
create table market_data (
    trade_date date,
    ticker varchar(20),
    open numeric,
    high numeric,
    low numeric,
    close numeric,
    adj_close numeric,
    volume bigint,
    primary key (trade_date, ticker),
    foreign key (ticker) references assets(ticker)
);
