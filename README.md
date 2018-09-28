## To do

THIS IS LIKE AVITO

[ ] TFIDF on viewed pages (instead of crosstab)
[ ] Average and maximum Bayesian purchase rate per page
[ ] Average time between pages
[ ] Do monthly (or other) rankings of products (like a leaderboard), then aggregate the ranks of the viewed products
[ ] Number of clicks (with granular counts)
[ ] Session counts of the current day (and hour)
[ ] Daily activity ratio like section 4.1 [here](https://cs.stanford.edu/people/jure/pubs/pinterest-kdd16.pdf)
[ ] What happened on the last view
[ ] Did the person backtrack
[ ] Category interaction ratios
[ ] Compute price differences with the average (multiplicative difference makes it easy to include a period and is scale agnostic), then aggregate (to do it count group counts + product price over group mean price)
    [ ] try with `log1p`
    [ ] try Bayesian differences like [here](https://www.kaggle.com/c/avito-demand-prediction/discussion/59914)
[ ] Entropy of product sales over time

- Think about normalizing (stemming) product titles to do groupings (particularly price groupings).
- Try to do counts with `log1p` to remove outliers
