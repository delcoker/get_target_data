import awswrangler as wr
import pandas as pd

import config


# https://github.com/awslabs/aws-lambda-powertools-python/issues/924
def lambda_handler(event, context, target_data_service=config.target_data_service):
    request_body = get_payload(event)

    file_path = get_file_path(request_body)
    fe_product_growth = get_product_input_configurations(request_body)

    df = get_s3_file_object(file_path)

    target_data_df = target_data_service.get_target_data(fe_product_growth, df)
    print(target_data_df.columns)

    return {
        'statusCode': 200,
        'body': target_data_df.to_json(orient='records')
        # 'body': json.dumps(list(all_products))
    }


def get_s3_file_object(file_path):
    try:
        df = wr.s3.read_csv(file_path, error_bad_lines=False)
        print('s3 read SUCCESS')
    except:
        print('Error => using Book2.csv')
        df = pd.read_csv("Book2.csv", error_bad_lines=False)
    return df


def get_product_input_configurations(request_body):
    try:
        fe_product_growth = request_body['payload']
    except:
        fe_product_growth = {"data": [{"product": "Product 1", "growth": 65},
                                      {"product": "Product 2", "growth": 35},
                                      {"product": "Product 3", "growth": 40}]}
    return fe_product_growth


def get_file_path(request_body):
    try:
        file_path = request_body['path']
    except:
        print('could not get s3 file path')
        S3_BUCKET_NAME = 'c-model-dev'
        S3_FILE_KEY = 'prototype/textCompany/Book2.csv'
        file_path = f"s3://{S3_BUCKET_NAME}/{S3_FILE_KEY}"
    return file_path


def get_payload(event):
    try:
        request_body = event["body"]
        return request_body
    except:
        print('could not get request body')
        pass


print(lambda_handler(None, None))
