import os

# set up the agent
MAX_REPLY = 10

# set up the LLM for the agent
os.environ["AUTOGEN_USE_DOCKER"] = "False"
# llm_config={"cache_seed": None, "config_list": [{"model": "gpt-4o", "temperature": 0.0, "api_key": os.environ.get("OPENAI_API_KEY")}]}
#Qwen/Qwen2-VL-2B
# llm_config = {
#     "cache_seed": None,
#     "config_list": [
#         {
#             "model": "Qwen/Qwen2-VL-2B",  # Replace with the correct model identifier
#             "temperature": 0.0,
#             "api_key": os.environ.get("API_KEY", "EMPTY"),  # Assuming no key is needed, use "EMPTY"
#             "model_server": "http://localhost:8091/v1",  # URL of your vLLM server
#         }
#     ]
# }

llm_config = {
    "cache_seed": None,
    "config_list": [
        {
            "model": "Qwen/Qwen2-VL-2B-Instruct",
            "temperature": 0.0,
            "api_key": os.environ.get("API_KEY", "EMPTY"),
            "base_url": "http://localhost:8091/v1",  
        }
    ]
}
# use this after building your own server. You can also set up the server in other machines and paste them here.
SOM_ADDRESS = "http://localhost:8092/"
GROUNDING_DINO_ADDRESS = "http://localhost:8093/"
DEPTH_ANYTHING_ADDRESS = "http://localhost:8094/"
