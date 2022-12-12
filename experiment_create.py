import yaml
import logging

from jmapc import Client
from jmapc.logging import log
from jmapc.fastmail import MaskedEmail, MaskedEmailSet

logging.basicConfig()
# Set jmapc log level to DEBUG
log.setLevel(logging.DEBUG)

CONFIG="testcred.yml"

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def createMaskedEmail(client):
	method = MaskedEmailSet(create=dict(
		foo= MaskedEmail(
			state="",
			for_domain="example.com",
			description="TEST for gopass-maskedemail",
			url="gopass websites/example.com",
			email_prefix="stefan"
		)
	))
	result = client.request(method)
	return result


def main():
	config = read_yaml(CONFIG)
	client = Client.create_with_api_token(
    	host=config["JMAP_HOST"], api_token=config["JMAP_API_TOKEN"]
	)

	result = createMaskedEmail(client)
	print(result)


if __name__ == '__main__':
	main()
