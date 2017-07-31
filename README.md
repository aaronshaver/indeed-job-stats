# indeed-job-stats
Uses Python, AWS Lambda, DynamoDB to track stats for job titles from Indeed.com

## Trigger

Cron expression for CloudWatch Event to use as a trigger in the Lambda function:

cron(0 13 * * ? *)

This will run every day at 6 AM PDT (1 PM UTC)

## Policy for IAM Role for the Lambda function to use

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "arn:aws:logs:*:*:*"
            },
            {
                "Sid": "AllowAccessToDynamo",
                "Effect": "Allow",
                "Action": [
                    "dynamodb:GetItem",
                    "dynamodb:BatchGetItem",
                    "dynamodb:Query",
                    "dynamodb:PutItem",
                    "dynamodb:UpdateItem",
                    "dynamodb:DeleteItem",
                    "dynamodb:BatchWriteItem"
                ],
                "Resource": [
                    "arn:aws:dynamodb:us-west-2:192460637947:table/JobTitleCounts"
                ]
            }
        ]
    }
