from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="sqlfluff1970",
    description="Repro of https://github.com/sqlfluff/sqlfluff/issues/1970",
    python_requires="~=3.9",
    packages=find_packages(exclude=["tests"]),
    package_data={
        '': ['py.typed'],
    },
    include_package_data=True,
    install_requires=["dbt-postgres==1.0.1"],
    extras_require={
        "dev": [
            "sqlfluff==0.9.1",
            "sqlfluff-templater-dbt==0.9.1"
        ]
    },
)
