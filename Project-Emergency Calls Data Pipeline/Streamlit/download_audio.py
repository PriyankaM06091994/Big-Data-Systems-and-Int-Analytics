import boto3


def download():
    s3 = boto3.resource('s3')

    # Replace with your bucket name and download directory
    bucket_name = s3.Bucket('amazon-connect-4735ee648c9d')
    path = './data/'

    # Download file into your download directory (/data)
    for s3_object in bucket_name.objects.all():
        file_path = s3_object.key
        filename = file_path.split("/")[6]
        bucket_name.download_file(file_path, path + filename)

    return
