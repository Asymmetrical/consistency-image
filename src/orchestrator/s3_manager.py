import boto3
import os
import uuid
import time
from typing import Optional
from dotenv import load_dotenv

def upload_to_s3(local_path: str, bucket_name: Optional[str] = None, prefix: str = "lab-ingest") -> Optional[str]:
    """
    Uploads a local image to S3 and returns a presigned URL.
    """
    load_dotenv(".env.local")
    
    bucket = bucket_name or os.getenv("S3_BUCKET")
    if not bucket:
        print("Error: S3_BUCKET not found in environment.")
        return None

    s3_client = boto3.client('s3', region_name=os.getenv('AWS_DEFAULT_REGION', 'eu-west-1'))
    
    file_name = os.path.basename(local_path)
    # Use a unique key to avoid collisions
    object_name = f"{prefix}/{int(time.time())}_{uuid.uuid4().hex[:8]}_{file_name}"
    
    try:
        print(f"--- S3 Manager: Uploading {file_name} to s3://{bucket}/{object_name} ---")
        s3_client.upload_file(local_path, bucket, object_name)
        
        # Generate a Presigned URL (Valid for 1 hour)
        url = s3_client.generate_presigned_url('get_object',
                                              Params={'Bucket': bucket,
                                                      'Key': object_name},
                                              ExpiresIn=3600)
        return url
    except Exception as e:
        print(f"S3 Upload Failed: {str(e)}")
        return None

if __name__ == "__main__":
    # Quick test if a file exists
    test_file = "data/references/kael_portraits/kael_anchor.png"
    if os.path.exists(test_file):
        url = upload_to_s3(test_file)
        if url:
            print(f"Success! Presigned URL: {url[:60]}...")
        else:
            print("Upload failed.")
    else:
        print(f"Test file not found: {test_file}")
