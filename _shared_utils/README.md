# README

**brought over from [cal-itp/data-analysis/_shared_utils](https://github.com/cal-itp/data-analyses/tree/main/_shared_utils)**
</br></br>
**did not bring over python files that were not needed (incl: dask_utils; gtfs_dataset_name_to_analysis_name; gtfs_utils_v2; portfolio_utils; schedule_rt_utils; rt_utils;  publish_utils; rt_dates; time_helpers; v1_rt_dates; webmap_utils)**

For analysis, there are probably a set of steps in data cleaning or visualization that analysts repeat. We encounter them both *within* a research question and *across* research questions. Why reinvent the wheel?

These shared utility functions are quality-of-life improvements for analysts as they iterate over their data cleaning and visualization steps. The utility functions would be importable across all directories in the `data-analyses` repo and can be called within a Jupyter notebook or Python script.

## Getting Started

1. From the repo root (`data-analyses/`), run `make install_env` (runs `uv sync --all-groups` + pre-commit setup)
2. In JupyterHub, select the **"Pyproject Local"** kernel when opening a notebook
3. Within Jupyter Notebook or script: `import shared_utils`
