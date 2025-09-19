PEMMA — CT/PET Segmentation with (Swin-)UNETR

[![Status](https://img.shields.io/badge/status-active-success)](#)
![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen)
![PyTorch](https://img.shields.io/badge/PyTorch-%F0%9F%A7%AA-red)
![MONAI](https://img.shields.io/badge/MONAI-💛-yellow)
![License](https://img.shields.io/badge/license-TBD-lightgrey)

> Training code & configs for UNETR/Swin-UNETR on CT/PET (HECKTOR). Includes utilities for ViT/LoRA experiments and multi-center setups.

---

## ✨ Highlights
- **UNETR / Swin-UNETR training** with ready-to-use YAML configs (`swin_unetr.yaml`, `train_ct.yaml`, `finetune_ctpet.yaml`).
- **CT-only or CT+PET** pipelines (e.g., `4Centers-CTPET.py`) for multi-center experiments.
- **ViT + LoRA helpers** (`LoraVit.py`, `LoravitCTweights.py`) for lightweight adaptation.
- Fully **Python** codebase and `requirements.txt` for one-shot setup.

> See `scripts/*.py` and top-level files such as `4Centers-CTPET.py`, `swin_unetr.yaml`, `finetune_ctpet.yaml`, `LoraVit.py`. (File names may evolve and more to be added.)
