from setuptools import setup

setup(
    name="cli-tasks",
    version="0.1",
    packages=["cli_tasks"],
    install_requires=[
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib",
    ],
    entry_points={
        "console_scripts": [
            "task = cli_tasks.main:main",
        ],
    },
)
