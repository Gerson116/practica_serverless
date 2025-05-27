
def lambda_hola_mundo(event, context):
    print(f'event {event}')
    print(f'context {context}')
    return {
        "statusCode": 200,
        "body": "¡Hola desde Lambda con CDK!"
    }
