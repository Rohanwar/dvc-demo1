import os

os.path.join

dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]


for d in dirs:
    os.makedirs(d,exist_ok=True)
    with open(os.path.join(d,".gitkeep"), "w") as  f:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")



]

for file in files:
    with open(file,"w") as f:
        pass