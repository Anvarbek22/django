
from sinch import SinchClient

sinch_client = SinchClient(
    key_id="",
    key_secret="",
    project_id="12"
)

send_batch_response = sinch_client.sms.batches.send(
    body="Hello from Sinch!",
    to=["+998919169262"],
    from_="+99899481977",
    delivery_report="none"
)

print(send_batch_response)