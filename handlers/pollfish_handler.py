#
# Verify a completed survey from S2S Callbacks
#
from flask import request


def verify():
    # Get all parameters from S2S Callback
    #
    # We're using a few of the query strings here, you can define more in your dashboard.
    #
    device_id = request.args.get('device_id')
    cpa = request.args.get('cpa')
    request_uuid = request.args.get('request_uuid')
    timestamp = request.args.get('timestamp')
    tx_id = request.args.get('tx_id')

# TODO Make handler code here
