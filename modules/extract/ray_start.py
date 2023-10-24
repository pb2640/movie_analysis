import ray 


ENV_VARIABLES = {
    "RAY_ENABLE_WINDOWS_OR_OSX_CLUSTER": "1"
}

my_runtime_env = {"env_vars": ENV_VARIABLES}
ray.init(runtime_env=my_runtime_env)
