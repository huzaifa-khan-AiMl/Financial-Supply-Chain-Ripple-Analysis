# Financial Supply Chain Ripple Analysis

An exploratory financial data science project investigating whether a significant
2018 decline in Apple was reflected across related upstream companies in its
supply chain, and how the timing and magnitude of those movements compared with
the broader technology sector.

## Background

In 2018, Apple experienced a slowdown in demand for its products, particularly
as consumers became less willing to purchase new iPhones at higher prices.
This contributed to pressure on Apple's business and raised concerns about the
broader effects on companies connected to Apple's supply chain.

Apple depends on companies such as Qualcomm for chips and Corning for glass
components. Because these companies operate upstream in the supply chain, a
reduction in Apple's demand could potentially affect them as well.

This raises an interesting financial question:

**Did the impact appear first in Apple, reach its upstream suppliers later, or
were the companies affected at approximately the same time?**

We will also compare these movements with the broader technology sector using
XLK to determine whether the decline was specific to Apple's ecosystem or part
of a wider technology-market movement.

## Research Question

Did a significant decline in Apple propagate through related upstream companies
such as Qualcomm and Corning?

Specifically:

- Did Apple, Qualcomm, and Corning decline at the same time?
- Did the movement appear first in Apple or in its upstream suppliers?
- Did the effect appear with a lag?
- Was the movement specific to this supply-chain ecosystem, or was it part of a
  broader technology-sector decline?
- When did the companies begin recovering after the decline?

## Assets

| Ticker | Company / Asset | Role |
|--------|------------------|------|
| AAPL | Apple | Focal company |
| QCOM | Qualcomm | Upstream supplier |
| GLW | Corning | Upstream supplier |
| XLK | Technology Select Sector SPDR Fund | Sector benchmark |

## Project Scope

The initial dataset will cover approximately:

**January 2017 → early 2020**

This period provides:

- Pre-event baseline
- 2018 shock period
- Post-event behavior
- Recovery period
- Context before the major COVID-19 market disruption

The exact event and analysis windows will be determined after inspecting and
validating the retrieved data rather than being assumed beforehand.

## Planned Workflow

1. Retrieve historical market data
2. Validate and inspect the raw data
3. Design the data schema
4. Store and query the data using PostgreSQL
5. Perform exploratory data analysis
6. Calculate returns and other derived metrics
7. Identify significant movements/events
8. Analyze timing and relationships between assets
9. Compare the assets against XLK
10. Investigate the post-event recovery
11. Document findings and limitations

## Data

Historical OHLCV market data will be collected for:

- AAPL
- QCOM
- GLW
- XLK

Derived metrics will be calculated separately from the raw data to preserve the
original dataset.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- PostgreSQL
- SQL
- yfinance / financial market data API

## Project Status

🚧 **In Progress**

The repository currently contains the initial project definition. Data
collection and analysis have not yet been completed.

## Limitations

This project focuses on a single Apple-related supply-chain example and does
not attempt to represent the entire smartphone industry.

XLK is used as a sector benchmark rather than a perfectly independent control,
since Apple itself is included in the ETF.

Other macroeconomic and company-specific factors may also influence stock
movements, so observed relationships should not automatically be interpreted
as proof of causation.
