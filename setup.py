from pathlib import Path
from setuptools import find_packages, setup

import torch

PROJECT_NAME = "ThreeDVG"
PACKAGE_NAME = PROJECT_NAME.replace("-", "_")
DESCRIPTION = "Visual Ground"

TORCH_VERSION = [int(x) for x in torch.__version__.split(".")[:2]]
assert TORCH_VERSION >= [1, 12], "Requires PyTorch >= 1.12"


if __name__ == "__main__":
    version = "0.1.10"

    print(f"Building {PROJECT_NAME}-{version}")

    setup(
        name=PROJECT_NAME,
        version=version,
        author="Yinjie Zhao",
        author_email="630877986@qq.com",
        url=f"https://github.com/yjzhao19981027/{PROJECT_NAME}",
        download_url=f"https://github.com/yjzhao19981027/{PROJECT_NAME}/tags",
        description=DESCRIPTION,
        long_description=Path("README.md").read_text(),
        long_description_content_type="text/markdown",
        packages=find_packages(exclude=("tests",)),
        include_package_data=True,
        package_data={PACKAGE_NAME: ["ThreeDVG/data/scannet/meta_data/*.txt", "ThreeDVG/data/scannet/meta_data/*.txt.gz", 
        "ThreeDVG/data/scannet/meta_data/*.csv", "ThreeDVG/data/scannet/meta_data/*.npz", 
        "ThreeDVG/data/scannet/meta_data/*.tsv", ".ThreeDVG/data/scannet/meta_data/*.p"]},
        zip_safe=False,
        python_requires=">=3.7",
        install_requires=[
            "pillow",
            "easydict",
            "fastapi",
            "h5py",
            "plyfile",
            "trimesh",
        ],
    )
