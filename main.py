import argparse
import time

from dotenv import dotenv_values

from amflowtest.client import APIClient
from amflowtest.definitions import batch, part

config = dotenv_values(".env")
parser = argparse.ArgumentParser(
    prog="AM-Vision test",
    description="test am flow api",
)
parser.add_argument(
    "-d",
    "--delete",
    action="store_true",
    help="Delete previous batch and print objects",
)


def main():
    args = parser.parse_args()
    delete = args.delete
    api = APIClient(url=config["AMV_URL"], token=config["AMV_TOKEN"])
    if delete:
        api.print.delete(id="bus")
        api.batch(1).delete()

    # Upload model if not already there
    response = api.design_reference.search.post({"id": "bus"})
    if not response["results"]:
        # upload stl model
        with open("bus.stl", "rb") as stl:
            api.design_reference.post({"id": "bus", "unit": "cm"}, files={"stl": stl})

    # define print (part)
    api.print.post(part)
    # define batch
    api.batch.post(batch)

    # register webhook
    api.webhook.post(
        {
            "event": "scan.assign",
            "target": config["WEBHOOK_URL"],
        }
    )


if __name__ == "__main__":
    main()
