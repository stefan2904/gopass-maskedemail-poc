import yaml

from jmapc import Client
from jmapc.fastmail import MaskedEmailGet

CONFIG="testcred.yml"

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def getMaskedEmails(client):
	method = MaskedEmailGet(ids=None)
	result = client.request(method)
	return result.data


def main():
	config = read_yaml(CONFIG)
	client = Client.create_with_api_token(
    	host=config["JMAP_HOST"], api_token=config["JMAP_API_TOKEN"]
	)

	result = getMaskedEmails(client)
	result = '\n\n'.join(map(lambda mm: "- {}".format(mm), result))
	print(result)


if __name__ == '__main__':
	main()
