# Session 9 Homework Reference Notes

## Colab notebook

Students should submit a link to their own Colab notebook.

## Expected work

A complete homework submission should:

- use PySpark instead of pandas for the main analytics work
- load `service_events.csv` with an explicit schema
- print schema, row count, and column names
- create the required derived columns and time features
- register the view as `service_events_enriched`
- include at least six Spark SQL queries
- include at least three grouped summaries
- include at least two sorted rankings
- include at least one time-based query
- use a Spark window function for ranking
- save `results/service_summary.csv`
- explain at least three findings in plain English
- stop Spark at the end

## Example feedback

Strong submissions connect the code output to meaning. For example, "Payments had the highest average error rate, so it may need reliability investigation" is better than "I grouped by service."

Strong submissions also explain how the same Spark workflow can be reused in the final project with symbols, price movement, volume, trade count, and trade time.
