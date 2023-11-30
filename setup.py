import setuptools

setuptools.setup(
    name='wqp',
    version='0.1.0',
    author='my_email@email.com',
    description='Wine quality predictor - a packaged machine learning algorithm to predict wine quality',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn==1.3.2",
        "pandas==2.1.3"
    ]
