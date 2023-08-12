from setuptools import setup

setup(
    name='mypass-tokens',
    version='1.0.0',
    description='SQL-like language for MyPass',
    license='MIT',
    packages=['mypass_tokens', 'mypass_tokens.git', 'mypass_tokens.command', 'mypass_tokens.sql'],
    package_dir={'mypass_tokens': 'mypass'},
    install_requires=[],
    package_data={'': ['license']}
)
