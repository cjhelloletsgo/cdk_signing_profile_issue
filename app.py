#!/usr/bin/env python3
import os

import aws_cdk as cdk

from issue.issue_stack import IssueStack2


app = cdk.App()
issue_stack = IssueStack2(
    app,
    "IssueStack2",
)


# deploy the stack, then uncomment the line below and the deployment will fail
# cdk.Tags.of(issue_stack).add("Project", "ethics")


app.synth()
