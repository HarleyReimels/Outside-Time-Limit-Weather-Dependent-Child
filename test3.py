import re

def find_eid(report):
    pattern = r'\b[A-Z]-\d{7,8}\b'
    result = re.findall(pattern, report)
    return result

print(find_eid("Employees B-1234567 and C-12345678 worked with products X-123456 and Z-123456789"))  # Should return ['B-1234567', 'C-12345678']
print(find_eid("Employees B-1234567 and C-12345678, not employees b-1234567 and c-12345678"))  # Should return ['B-1234567', 'C-12345678']
