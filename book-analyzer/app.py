import logging

from chalice import Chalice

from chalicelib.analyze import analyze_book

# Your public bucket from Lab 06: change mst3k to your computing ID
BUCKET = "public-eax9zh"

app = Chalice(app_name="book-analyzer")
# Show the logger.info lines of analyze.py in CloudWatch
logging.getLogger().setLevel(logging.INFO)


@app.on_s3_event(bucket=BUCKET, events=["s3:ObjectCreated:*"], suffix=".txt")
def analyze_new_book(event):
    """Analyze a book when it is uploaded to BUCKET."""
    analyze_book(event.bucket, event.key)