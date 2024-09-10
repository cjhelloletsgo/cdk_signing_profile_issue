from aws_cdk import (
    Stack,
    Duration,
    BundlingOptions,
)
from aws_cdk import aws_lambda as lambda_
from aws_cdk import (
    aws_signer as signer,
)
from constructs import Construct


class IssueStack2(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        signing_profile = signer.SigningProfile(
            self,
            "Signing Profile",
            platform=signer.Platform.AWS_LAMBDA_SHA384_ECDSA,
        )

        code_signing_config = lambda_.CodeSigningConfig(
            self,
            "Code Signing Config",
            signing_profiles=[
                signing_profile,
            ],
            description=f"CDK Signing Config for {Stack.of(self).stack_name}",
            untrusted_artifact_on_deployment=lambda_.UntrustedArtifactOnDeployment.WARN,
            # Changing untrusted_artifact_on_deployment will cause a deployment error https://github.com/aws/aws-cdk/issues/29474
            # untrusted_artifact_on_deployment=lambda_.UntrustedArtifactOnDeployment.ENFORCE,
        )

        lambda_.Function(
            self,
            "Error Example Lambda",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="lambda_function.lambda_handler",
            code_signing_config=code_signing_config,
            code=lambda_.Code.from_asset(
                "lambda/error_example",
            ),
            environment={},
            description="This is an example lambda to show a signing profile failure.",
            timeout=Duration.seconds(3),
            memory_size=256,
            architecture=lambda_.Architecture.X86_64,
            retry_attempts=0,
            # logging_format=lambda_.LoggingFormat.JSON,
            # application_log_level="INFO",
            tracing=lambda_.Tracing.DISABLED,
            events=[],
            initial_policy=[],
        )
