### Directory: globe-guard-ai-disaster-forecaster

# === File: lambda/forecast_generator.py ===
import boto3
import json
import os

def lambda_handler(event, context):
    location = event.get("location", "your area")
    alert_type = event.get("alert", "earthquake")
    magnitude = event.get("magnitude", 6.1)

    prompt = (
        f"An alert of a {alert_type} has been received for {location}. "
        f"The event magnitude is {magnitude}. "
        "Generate a natural language summary of expected impact including infrastructure damage, power loss, and response status."
    )

    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

    body = {
        "prompt": prompt,
        "max_tokens_to_sample": 200,
        "temperature": 0.7
    }

    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2",
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json"
    )

    forecast = json.loads(response["body"].read())
    summary = forecast.get("completion", "No forecast generated.")

    print("Generated Forecast:", summary)

    return {
        "statusCode": 200,
        "body": json.dumps({"forecast": summary})
    }


# === File: eventbridge/disaster_event_rule.json ===
{
  "Name": "DisasterTriggerRule",
  "ScheduleExpression": "rate(30 minutes)",
  "State": "ENABLED",
  "Targets": [
    {
      "Arn": "arn:aws:lambda:us-east-1:123456789012:function:forecast_generator",
      "Id": "DisasterEventTarget"
    }
  ]
}


# === File: api_gateway/api_config.json ===
{
  "openapi": "3.0.1",
  "info": {
    "title": "GlobeGuard API",
    "version": "1.0"
  },
  "paths": {
    "/submit": {
      "post": {
        "x-amazon-apigateway-integration": {
          "uri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:forecast_generator/invocations",
          "httpMethod": "POST",
          "type": "aws_proxy"
        },
        "responses": {
          "200": {
            "description": "Success"
          }
        }
      }
    }
  }
}


# === File: README.md ===
# GlobeGuard – AI-Powered Geo-Disaster Impact Forecaster

GlobeGuard is a serverless application that delivers location-based disaster forecasts using AI.

## How It Works
- User submits a location via API Gateway
- Disaster alert (real/simulated) triggers Lambda via EventBridge
- Lambda formats a prompt and sends it to Amazon Bedrock (Claude)
- Claude returns a natural-language impact summary
- Lambda prints the forecast, sends it via SES, or stores it in S3

## AWS Lambda Usage
Lambda is used to:
- Process event data
- Invoke Bedrock with a formatted prompt
- Return the AI-generated summary
- Triggered by both EventBridge and API Gateway

## Built With
- AWS Lambda
- Amazon API Gateway
- Amazon EventBridge
- Amazon Bedrock (Claude)
- Amazon S3
- Amazon SES
- IAM
- CloudWatch
- Python (Boto3)

## License
MIT License
