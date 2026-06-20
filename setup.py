from setuptools import setup, find_packages

setup(
    name="islamic-content-sdk",
    version="1.0.0",
    author="The Association for Multi-lingual Islamic Content",
    author_email="info@islamiccontent.sa",
    description="An integrated and easy-to-use software library to fetch authentic Islamic content (Holy Quran and Hadith) in multiple languages.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/2yousefreda/islamic-content-sdk-npm", # Or update when Py repository is ready
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
)
