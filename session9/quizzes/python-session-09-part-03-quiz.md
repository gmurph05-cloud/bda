# Session 9 Part 3 Quiz (Rankings and Summary Tables)

## Question 1

What does a one-row-per-service summary do?

- Aggregates many event rows into one summary row for each service
- Deletes all service rows
- Converts Spark into pandas
- Creates a virtual environment

Answer: 1
Type: single
Time: 50
Explanation: Grouped summaries make comparison easier.

## Question 2

Which function measures variability in latency?

- `stddev`
- `header`
- `to_date`
- `createView`

Answer: 1
Type: single
Time: 40
Explanation: `stddev` measures how spread out values are.

## Question 3

Which Spark feature is used to rank rows?

- Window functions
- CSV headers
- Virtual environments
- Markdown tables

Answer: 1
Type: single
Time: 45
Explanation: Window functions can rank rows based on ordered values.

## Question 4

What does `dense_rank` do?

- Assigns ranks, giving tied values the same rank without gaps
- Counts CSV columns
- Removes every duplicate service
- Stops Spark after each row

Answer: 1
Type: single
Time: 55
Explanation: `dense_rank` is useful for readable rankings.

## Question 5

What does `Window.partitionBy("service")` do in the busiest-hour calculation?

- Ranks hours separately for each service
- Combines all services into one string
- Deletes the service column
- Saves the DataFrame as CSV

Answer: 1
Type: single
Time: 55
Explanation: Partitioning by service creates a separate ranking group for each service.

## Question 6

Which rank should put the highest total traffic first?

- `traffic_rank`
- `reliability_rank`
- `event_id`
- `day_of_week`

Answer: 1
Type: single
Time: 45
Explanation: `traffic_rank` is ordered by total traffic descending.

## Question 7

Which rank should put the lowest average error rate first?

- `reliability_rank`
- `traffic_rank`
- `latency_variability_rank`
- `event_hour`

Answer: 1
Type: single
Time: 45
Explanation: The most reliable service has the lowest average error rate.

## Question 8

Why does Spark usually write CSV output as a folder?

- Spark is designed for distributed output with part files
- Spark cannot write text
- Spark only writes Word documents
- Spark deletes CSV files automatically

Answer: 1
Type: single
Time: 55
Explanation: Distributed jobs can write multiple part files into one output folder.

## Question 9

Which final project task is most similar to `traffic_rank`?

- Activity ranking
- Team 1 data collection
- Private repository setup
- Reflection writing

Answer: 1
Type: single
Time: 45
Explanation: Both rank entities by activity-related metrics.

## Question 10

Which final project task is most similar to `latency_variability_rank`?

- Volatility ranking
- Data download
- README formatting
- Pandas sampling only

Answer: 1
Type: single
Time: 45
Explanation: Both rank entities by variability.
