
import os
import aws_cdk as cdk
from stacks.cdk_hello_word import CdkHolaMundoStack

app = cdk.App()

hola_mundo_stack = CdkHolaMundoStack(
    app,
    construct_id="CdkHolaMundoStack",
    env={
        "account": os.getenv("CDK_DEFAULT_ACCOUNT"),
        "region": os.getenv("CDK_DEFAULT_REGION")
    },
    description="Stack de CDK para desplegar una función Lambda simple que retorna un saludo",
)

cdk.Tags.of(hola_mundo_stack).add("Environment", "Development")
cdk.Tags.of(hola_mundo_stack).add("RepositoryUrl", "https://github.com/Gerson116/practica_serverless")
cdk.Tags.of(hola_mundo_stack).add("Project", "Practica Serverless con CDK")
cdk.Tags.of(hola_mundo_stack).add("Owner", "Gerson116")

app.synth()