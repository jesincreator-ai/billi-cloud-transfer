import os
import tempfile
from pathlib import Path

import boto3
from huggingface_hub import HfApi, hf_hub_download

repos = [
    ("Chat2Find/Chat2Find-Corpus", "Chat2Find-Corpus"),
    ("heymeowcat/sinhala-commons", "sinhala-commons"),
    ("gopi30/english-tamil", "english-tamil"),
]

s3 = boto3.client(
    "s3",
    endpoint_url=os.environ["IDRIVE_ENDPOINT"],
    aws_access_key_id=os.environ["IDRIVE_ACCESS_KEY"],
    aws_secret_access_key=os.environ["IDRIVE_SECRET_KEY"],
    region_name=os.environ["IDRIVE_REGION"],
)

bucket = os.environ["IDRIVE_BUCKET"]
api = HfApi()

for repo, folder in repos:
    print("Starting:", repo)

    files = api.list_repo_files(
        repo_id=repo,
        repo_type="dataset"
    )

    for name in files:
        if name == ".gitattributes":
            continue

        with tempfile.TemporaryDirectory() as temp:
            local = hf_hub_download(
                repo_id=repo,
                filename=name,
                repo_type="dataset",
                local_dir=temp
            )

            key = f"datasets/{folder}/{name}"

            print("Uploading:", key)
            s3.upload_file(local, bucket, key)
            print("Uploaded:", key)

    print("Finished:", repo)

print("ALL DATASETS TRANSFERRED")

