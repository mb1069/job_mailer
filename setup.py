import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="job-mailer",  # Replace with your own username
    version="1.0.2",
    author="Miguel d'Arcangues Boland",
    author_email="migueldboland@gmail.com",
    description="Job mailer for long running jobs on remote servers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mb1069/job_mailer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'mailme = src.mail:main',
        ],
    },
)
