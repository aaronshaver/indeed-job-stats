# indeed-job-stats
Uses Python, AWS Lambda, DynamoDB to track stats for job titles from Indeed.com

Cron expression for CloudWatch Event to use as a trigger in the Lambda function:

cron(0 13 * * ? *)

This will run every day at 6 AM PDT (1 PM UTC)
