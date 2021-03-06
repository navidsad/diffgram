from diffgram import Project

project = Project(
			project_string_id = "replace_with_project_string",
			client_id = "replace_with_client_id",
			client_secret = "replace_with_client_secret"	)

brain = project.get_model(name = "my model")

# 3 different methods to do predictions

# Local
path = ""
inference = brain.predict_from_local(path)

# URL (Recommended over from local, works for cloud providers)
url = ""
inference = brain.predict_from_url(url)

# Project file
inference = brain.predict_from_file(file_id = 111546)

