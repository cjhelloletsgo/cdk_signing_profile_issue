import aws_cdk as core
import aws_cdk.assertions as assertions

from issue.issue_stack import IssueStack

# example tests. To run these tests, uncomment this file along with the example
# resource in issue/issue_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IssueStack(app, "issue")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
