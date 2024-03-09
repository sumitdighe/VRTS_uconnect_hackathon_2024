import requests
import json

INFRACOST_PRICING_ENDPOINT = "https://pricing.api.infracost.io/graphql"
INFRACOST_API_KEY = "ico-AS4Ut2vRV0rxwW8sk1ddHyjSfgSlRgCi"

headers = {
    "X-Api-Key": INFRACOST_API_KEY,
    "Content-Type": "application/json"
}

# Define the GraphQL query with region and productFamily filters
query = """
{
  products(filter: {
    vendorName: "aws",
    service: "AmazonEC2",
    region: "us-east-1",
    productFamily: "Compute Instance"
    attributeFilters: [
      {key: "instanceType", value: "m3.large"},
      {key: "operatingSystem", value: "Linux"},
      {key: "tenancy", value: "Shared"},
      {key: "capacitystatus", value: "Used"},
      {key: "preInstalledSw", value: "NA"}
    ]
  }) {
    prices(filter: {purchaseOption: "on_demand"}) {
      INR
    }
  }
}
"""
payload = {
    "query": query
}

response = requests.post(INFRACOST_PRICING_ENDPOINT, json=payload, headers=headers)

# Check response
if response.status_code == 200:
    data = response.json()
    print("Response:", data)
else:
    print("Error:", response.text)