
name: BILLI Dataset Cloud Transfer

on:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  transfer:
    name: Transfer datasets to IDrive e2
    runs-on: ubuntu-latest
    timeout-minutes: 360

    steps:
      - name: Get transfer program
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install required packages
        run: |
          python -m pip install --upgrade pip
          pip install huggingface_hub boto3

      - name: Transfer datasets
        env:
          IDRIVE_ENDPOINT: ${{ secrets.IDRIVE_ENDPOINT }}
          IDRIVE_BUCKET: ${{ secrets.IDRIVE_BUCKET }}
          IDRIVE_ACCESS_KEY: ${{ secrets.IDRIVE_ACCESS_KEY }}
          IDRIVE_SECRET_KEY: ${{ secrets.IDRIVE_SECRET_KEY }}
          IDRIVE_REGION: ${{ secrets.IDRIVE_REGION }}
        run: python transfer.py
