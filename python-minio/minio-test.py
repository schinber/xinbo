from minio import Minio
from minio.error import ResponseError

minioClient = Minio('192.168.216.130:9000',
                    access_key='minioadmin',
                    secret_key='minioadmin',
                    secure=False)
try:
    minioClient.make_bucket("mybucket", location="us-east-1")
except ResponseError as err:
    print(err)