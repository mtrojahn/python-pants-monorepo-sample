pex_binary(
    name="app",
    entry_point="app.py",
    # this is required only if we want to run the docker images locally on a mac
    # because they are build using ubuntu images
    platforms=["linux-x86_64-cp-39-cp39m", "macosx_10.9-x84_64-cp-39-cp39m"],
)

python_sources()

docker_image(name="another_api_image", dependencies=[":app"])
