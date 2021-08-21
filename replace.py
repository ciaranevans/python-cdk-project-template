import sys
import re


def replace(project_name: str):
    for file in ["cdk/app.py", "cdk/stack.py", "README.md"]:
        with open(file, "r+") as f:
            content = f.read()
            content = re.sub('TemplateProject', project_name, content)
            f.seek(0)
            f.write(content)
            f.truncate()


if __name__ == "__main__":
    replace(sys.argv[1])
