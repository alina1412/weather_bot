run:
	poetry run python -m bot_service

lint:
	isort bot_service tests
	black bot_service tests
	