# DevOps-Scripts
Scripts for performing/automating DevOps actions and processes (python & bash)

- ### repo_auth_config.py (Linux)
    ```
    This Python script configures the requirements needed for authenticating with the following online repositories: 
    AWSCodeCommit (SSH & HTTPS-GRC), Azure-DevOps Repo (SSH), GitHub (SSH), BitBucket(SSH)
    ```

- ### lambda_version_incrementer.py (Aws-Lambda)
    ```
    This Python Lambda function increments the version passed to it and returns a new version. It takes 2 query parameters which are:
        - accesskey : Set your accesskey as an environment variable in the "configuration" tab of your lambda function. Change this value
        to restrict access.
        - versiondetails : This query parameter takes the current version (semantic verion) which is separated by a Boolean incrementer determiner 
        (Ex: 4.1.0|false.false.true) and returns a new semantic version. The incrementation is performed from left to right (i.e from major to patch)
        
    URL schema:
    https://<LAMBDA_FUNCTION_URL>?accesskey={accesskey}&versiondetails={versiondetails}
    Note: Don't forget to encode your URL.
    ```

- ### repo_auth_config.py (Python & Terraform)
    * *Coming...*
