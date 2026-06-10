# Session 9 Part 2 Quiz (Derived Columns and Time Features)

## Question 1

Which method adds or replaces a Spark DataFrame column?

- `makeColumn`
- `withColumn`
- `add_cell`
- `installColumn`

Answer: 2
Type: single
Time: 40
Explanation: `withColumn` returns a DataFrame with the new or replaced column.

## Question 2

Which expression calculates `total_bytes`?

- `service + region`
- `event_time / service`
- `bytes_in + bytes_out`
- `latency_ms - service`

Answer: 3
Type: single
Time: 40
Explanation: Total bytes are incoming bytes plus outgoing bytes.

## Question 3

Why does the tutorial calculate `error_rate` only when `request_count > 0`?

- To sort services alphabetically
- To stop Spark
- To remove timestamp columns
- To avoid division by zero

Answer: 4
Type: single
Time: 50
Explanation: Safe division prevents errors or invalid results when the denominator is zero.

## Question 4

Which function extracts the hour from a timestamp column?

- `hour`
- `weekday`
- `schema`
- `rank`

Answer: 1
Type: single
Time: 40
Explanation: `hour(col("event_time"))` extracts the hour value.

## Question 5

Which function converts a timestamp into a date?

- `to_folder`
- `to_date`
- `to_schema`
- `to_rank`

Answer: 2
Type: single
Time: 40
Explanation: `to_date` extracts the date part from a timestamp.

## Question 6

What does `when(...).otherwise(...)` help create?

- A permanent database
- A virtual environment
- Conditional values such as `latency_band`
- A CSV header

Answer: 3
Type: single
Time: 50
Explanation: `when` is used for conditional column logic.

## Question 7

Which SQL query finds total requests by hour?

- `SELECT event_hour FROM service_events_enriched STOP BY request_count`
- `SUM event_hour USING request_count`
- `GROUP request_count FROM event_hour`
- `SELECT event_hour, SUM(request_count) FROM service_events_enriched GROUP BY event_hour`

Answer: 4
Type: single
Time: 60
Explanation: The query groups rows by hour and sums request counts.

## Question 8

Which final project feature is most similar to `event_hour`?

- `symbol`
- `trade_hour`
- `close`
- `price_range`

Answer: 2
Type: single
Time: 45
Explanation: Both are hour features extracted from timestamp columns.

## Question 9

Which final project feature is most similar to `latency_band`?

- `quote_volume`
- `open_time`
- `candle_direction`
- `trade_count`

Answer: 3
Type: single
Time: 45
Explanation: Both are category labels created from row-level conditions.

## Question 10

Why register `service_events_enriched` after creating derived columns?

- So the raw CSV is deleted
- So Java is installed
- So Spark no longer needs memory
- So SQL queries can use the new columns

Answer: 4
Type: single
Time: 50
Explanation: Registering the enriched DataFrame lets Spark SQL query the derived columns.
