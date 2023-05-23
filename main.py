from llama_cpp.server.app import create_app, Settings


import tomllib



with open("config.toml", "rb") as f:
    settings = tomllib.load(f)

settings = Settings(**settings)

app = create_app(settings=settings)

