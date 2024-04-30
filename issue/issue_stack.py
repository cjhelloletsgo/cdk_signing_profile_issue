from aws_cdk import (
    Stack,
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
        )
