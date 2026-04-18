from mlx_lm.utils import snapshot_download

snapshot_download(
    repo_id="mlx-community/GLM-OCR-6bit",
    local_dir="./models/glm-ocr-6bit",
    local_dir_use_symlinks=False,
)