import  setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="SWSummarizer"
AUTHOR_USER_NAME="JhilMilSitara"
SRC_REPO="SessionWise Summarizer"
AUTHOR_EMAIL="ml.joshaaeee@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A NLP based Text Summarizer",
    #long_description=  long_description,
    long_description_content="text/markdown",
    url=f"https://guthub.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)

