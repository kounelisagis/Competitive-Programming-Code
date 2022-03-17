import glob
import parser, solver, writer
import argparse

parser = argparse.ArgumentParser()
required = parser.add_argument_group("required arguments")

required.add_argument(
    "-f",
    "--file",
    help="use this to choose which dataset file to use",
    required=True,
)

args = parser.parse_args()
filename = args.file


dataset = parser.parse(f'datasets/{filename}')
solution = solver.solve(dataset)
writer.write(solution, 'solutions/'+filename)
