from setuptools import setup, find_packages

setup(
    name="media2025",
    version="0.1.0",
    description="SwinUNETR for 3D Medical Imaging with PEFT/LoRA",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/MedIA2025",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "monai>=1.2.0",
        "numpy>=1.22.0",
        "peft>=0.4.0",
        "transformers>=4.30.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
) 