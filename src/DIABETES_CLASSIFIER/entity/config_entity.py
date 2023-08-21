from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataingestionConfig:
    root_dir : Path
    source_dir: Path
    train_dir : Path
    test_dir : Path

@dataclass(frozen=True)
class Data_TransformationConfig:
    root_dir:Path
    preprocessor_dir:Path

@dataclass
class Model_trainerConfig:
    root_dir :Path
    model_dir :Path