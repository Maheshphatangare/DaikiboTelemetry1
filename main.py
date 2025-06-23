
import json
from datetime import datetime

def convert_format_1(data):
    """
    Convert data from format 1 (data-1.json) to the unified format (data-result.json).
    Format 1 has ISO timestamp which needs to be converted to milliseconds.
    """
    result = []
    for item in data:
        # Parse ISO timestamp and convert to milliseconds since epoch
        iso_time = item['timestamp']
        dt = datetime.fromisoformat(iso_time.replace('Z', '+00:00'))
        timestamp_ms = int(dt.timestamp() * 1000)
        
        # Create unified format dictionary
        converted = {
            'timestamp': timestamp_ms,
            'machine_id': item['machineId'],
            'status': item['status'],
            'temperature': item['temperature'],
            'pressure': item['pressure'],
            'vibration': item['vibration']
        }
        result.append(converted)
    return result

def convert_format_2(data):
    """
    Convert data from format 2 (data-2.json) to the unified format (data-result.json).
    Format 2 already uses milliseconds timestamp, so no conversion needed for timestamp.
    """
    result = []
    for item in data:
        # Create unified format dictionary
        converted = {
            'timestamp': item['timestamp_ms'],
            'machine_id': item['machine'],
            'status': item['state'],
            'temperature': item['temp'],
            'pressure': item['press'],
            'vibration': item['vib']
        }
        result.append(converted)
    return result

# Main execution for testing
if __name__ == "__main__":
    # Load input data
    with open('data-1.json', 'r') as f:
        data1 = json.load(f)
    with open('data-2.json', 'r') as f:
        data2 = json.load(f)
    
    # Convert both formats
    result1 = convert_format_1(data1)
    result2 = convert_format_2(data2)
    
    # Combine results
    combined = result1 + result2
    
    # Sort by timestamp to ensure consistent ordering
    combined.sort(key=lambda x: x['timestamp'])
    
    # Output result
    with open('output.json', 'w') as f:
        json.dump(combined, f, indent=2)
