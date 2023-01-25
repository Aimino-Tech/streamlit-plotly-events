import setuptools

setuptools.setup(
    name="streamlit-plotly-events-custom-data",
    version="0.0.6.3",
    author="Zafir Stojanovski",
    author_email="zafir.stojanovski@aimino.de",
    description="Plotly chart component for Streamlit that also allows for events to bubble back up to Streamlit. This is a fork that allows the user to specify custom_data in the plot.",
    long_description="Plotly chart component for Streamlit that also allows for events to bubble back up to Streamlit. This is a fork that allows the user to specify custom_data in the plot.",
    long_description_content_type="text/plain",
    url="https://github.com/Aimino-Tech/streamlit-plotly-events",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
        "plotly >= 4.14.3",
    ],
)
