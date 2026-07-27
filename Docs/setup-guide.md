# AWS Backup & Disaster Recovery Automation – Setup Guide

## Prerequisites
- AWS Account
- IAM User with Administrator Access
- Python 3.x
- Git
- VS Code

## Step 1
Launch an EC2 instance.

## Step 2
Create and attach an EBS volume.

## Step 3
Create an S3 bucket.

## Step 4
Create an IAM role with:
- AmazonEC2FullAccess
- AmazonS3FullAccess
- AmazonSNSFullAccess
- CloudWatchLogsFullAccess

## Step 5
Create the Lambda function.

## Step 6
Configure environment variables.

## Step 7
Create an EventBridge Scheduler.

## Step 8
Create an SNS topic and subscribe your email.

## Step 9
Test the Lambda function.

## Step 10
Verify:
- EBS snapshot
- S3 report
- CloudWatch logs
- SNS email