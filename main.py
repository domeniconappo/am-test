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
parser.add_argument("-d", "--delete", action="store_true")


def main():
    args = parser.parse_args()
    delete = args.delete
    api = APIClient(url=config["AMV_URL"], token=config["AMV_TOKEN"])
    if delete:
        api.print.delete(id="bus")
        api.batch(1).delete()

    # Check if the model was already uploaded
    response = api.design_reference.search.post({"id": "bus"})
    if not response["results"]:
        # upload stl model
        with open("bus.stl", "rb") as stl:
            api.design_reference.post({"id": "bus", "unit": "cm"}, files={"stl": stl})

    # define print (part)
    api.print.post(part)
    # define batch
    api.batch.post(batch)

    # wait for assignment
    assigned = False
    while not assigned:
        time.sleep(5)
        print("checking assignment...")
        res = api.scan_assignment.get(batch=batch["id"])
        assigned = any(scan["print"] == "bus" for scan in res["results"])

    # print date and time of assignment
    assignment_created = [assignment["created"] for assignment in res["results"] if assignment["print"] == "bus"][0]

    print("Part was assigned on: %s" % assignment_created)


if __name__ == "__main__":
    main()
