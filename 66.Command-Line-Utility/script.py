import argparse

# 1. Create the manager (Parser)
parser = argparse.ArgumentParser(description="A tool to greet users")

# 2. Tell the manager what to look for
# We add '--name' as a flag
parser.add_argument("--name", help="Enter your name here")
parser.add_argument("--job", help="Enter your profession", default="Programmer")

# 3. Collect the answers
args = parser.parse_args()

# Use the data
print(f"Hello {args.name}! You are a great {args.job}.")