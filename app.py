import os

from aws_cdk import core
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_s3_deployment import BucketDeployment, Source


class CdkAngularTemplateStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = Bucket(
            self,
            "CdkAngularTemplateBucket",
            website_index_document="index.html",
            public_read_access=True,
            removal_policy=core.RemovalPolicy.DESTROY,  # Stack削除と同時にバケットを削除する
        )
        BucketDeployment(
            self,
            "CdkAngularTemplateBucketDeployment",
            sources=[Source.asset( "cdk-angular-template/dist/cdk-angular-template")],
            destination_bucket=bucket
        )


app = core.App()
env = core.Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"), region="us-east-1")
CdkAngularTemplateStack(app, "cdk-angular-template", env=env)

app.synth()
