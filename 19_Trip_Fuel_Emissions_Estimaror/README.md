This project is a multi-stage function pipeline that calculates fuel used,fuel cost,and C02 emissions for a trip,then generates a formatted summary report.

#CONCEPTS PRACTICED
-A 4 Function pipeline with branching data flow:one function's output feeds into two separate downstream functions,which both then feed into a final reporting function
-Dictionary lookups for fuel price and emissions data by fuel type
-Input validation using a while loop to reject invalid dictionary keys
-Input normalization
-f-string formatted multi-line report output

#DEBUGGING LESSON
'calculate_emissions() initially returned "litres_used,c02_per_litre" as a tuple instead of the actual multiplication result.A reminder that returning multiple values is only correct when the caller genuinely needs multiple separate results,not when a single calculated number was the goal.

AUTHOR: ERICK KIROBI