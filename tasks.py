import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--task', type=str, required=True)

args = parser.parse_args()

print('Task added: ', args.task)
