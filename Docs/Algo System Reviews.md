# Algo System Reviews
v01
October 1 2017


## QSTrader
https://github.com/mhallsmoore/qstrader
https://www.quantstart.com/qstrader

### Cons
1. Shares only - assumes 2 decimal places
2. Bar actions occur on close only
2. Not fully decoupled messaging - some sequential processing
3. Backoffice and Statistics mixed in with trade processing - poor performance
4. Some code not optimised for performance
5. CSV only
6. Modules represent bank structure
7. No screener
8. No Indicators - code hem each time
9. No strategy parent class / overall manager

### Pros
1. Great Position class
2. Great Statistics class
3. Nice code beautification
4. Simple event system with Queue's
5. Integrates sentiment (not needed yet or reviewed)

### Notes
1. Uses int(price * 1e8) for floating point pricing
