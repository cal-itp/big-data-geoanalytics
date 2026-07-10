
add_precommit:
	pip install pre-commit
	pre-commit install

# install_env:
#	pip install uv && uv sync --all-groups
#	make add_precommit

install_env:
	pip install uv && uv sync --all-groups
	make add_precommit


uv_setup_project:
	pip install uv
	uv init
	uv add _shared_utils
    uv add calitp_data_analysis
	uv lock