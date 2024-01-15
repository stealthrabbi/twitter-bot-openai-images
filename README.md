# twitter-bot-openai-images
Image Open AI generator


## Development

Poetry can be used to manage dependencies locally. Poetry dependencies must be exported (synchronized) to `requirements.txt` if deploying to Azure app service for python applications,
as by default at least, it installs dependencies from requirements.txt when building the container.

To update requirements.txt, run

```sh
poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt
```

## Open AI - GPT based bot

<< FILL ME IN>>

## Deployment

You can deploy the servcie and run it periodically on Google Cloud.

1. Create a Cloud Function (serverless), and deploy the code there.
1. Create a Cloud Scheduler to hit the URL of your Cloud Function at some periodicity. Authentication should be enabled, and restrict authentication within your Google Cloud project's servcie account.