import os

from aws_cdk import (
    Stack,
    Duration,
    aws_lambda,
    CfnOutput,
)

from constructs import Construct

class CdkHolaMundoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.construct_id = construct_id

        #   Main method to create resources
        self.create_lambda_function()
        self.add_lambda_funtion_url()
        self.generate_cloudformation_outputs()

    def create_lambda_function(self):
        directorio = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        RUTA_FUNCION_FOLDER = os.path.join(
            directorio, "lambda_hola_mundo", "src"
        )

        self.simple_lambda = aws_lambda.Function(
            self,
            id="{}Lambda".format(self.construct_id),
            function_name="hola-mundo-lambda-function",
            description="Funcion Lambda Simple desplegada AWS con CDK",
            code=aws_lambda.Code.from_asset(RUTA_FUNCION_FOLDER),
            handler="lambda_hola_mundo",
            runtime=aws_lambda.Runtime.PYTHON_3_13,
            timeout=Duration.seconds(5),
            memory_size=128,
            environment={
                "LOG_LEVEL": "DEBUG"
            }
        )

        def add_lambda_funtion_url(self):
            self.lambda_function_url = self.simple_lambda.add_function_url(
                auth_type=aws_lambda.FunctionUrlAuthType.NONE
            )
            print(f"Lambda URL: {self.lambda_function_url.url}")

        def generate_cloudformation_outputs(self):
            CfnOutput(
                self,
                id="LambdaFunctionUrl",
                value=self.lambda_function_url.url,
                description="URL de la función Lambda"
            )
