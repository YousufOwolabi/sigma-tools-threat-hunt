from sigma.collection import SigmaCollection
from sigma.backends.splunk import SplunkBackend

# Path to your Sigma YAML rule file
sigma_rule_path = "/home/ghost/sigma-tools-threat-hunt/tools_threathunt.yml"

# Load Sigma rule(s) from YAML
with open(sigma_rule_path, "r") as f:
    collection = SigmaCollection.from_yaml(f)

# Initialize the Splunk backend
backend = SplunkBackend()

# Convert the Sigma rule(s) to Splunk queries
splunk_queries = backend.convert(collection)

# Print all resulting Splunk queries
for query in splunk_queries:
    print(query)
