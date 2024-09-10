#!/usr/bin/env python3
import aws_cdk as cdk

from issue.issue_stack import IssueStack2


app = cdk.App()
issue_stack = IssueStack2(
    app,
    "IssueStack2",
)


# deploy the stack, then uncomment the line below and the deployment will fail
# Update, with 2.157.0 (build 7315a59) I was able to deploy but removing this line will cause an error
cdk.Tags.of(issue_stack).add("Test", "THIS_WILL_CAUSE_AN_ERROR")


app.synth()
