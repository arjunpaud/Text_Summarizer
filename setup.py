import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description_content = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "arjunpaudel"
SRC_REPO = "Text_Summarizer"
AUTHOR_EMAIL = "paudela184@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer Package",
    long_description=long_description_content,
    long_description_content="text/markdown",
    url=f"https://github.com/arjunpaud/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/arjunpaud/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)