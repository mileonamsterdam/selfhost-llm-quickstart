
# setup
sudo dnf install nvidia-container-toolkit


## example dataset
datasets/
  solid/
    solid_principles.md
    examples.txt
    notes.md
  clean_code/
    chapter1.md
    chapter2.md

# run 
podman-compose up -d

# log
podman logs -f vllm-gemma
podman logs -f crewai-app
