from prefect import task
from prefect import Flow


@task
def extract():
    """Get a list of data"""
    return [1, 2, 3]


@task
def transform(data):
    """Lets sqaure of each input"""
    return [i * i for i in data]


@task
def load(data):
    """Display data to show we have received it """
    print("received data: {}".format(data))


with Flow('ETL') as flow:
    e = extract()
    t = transform(e)
    l = load(t)

flow.run()
flow.visualize()
