from huggingface_hub import snapshot_download

def main():
    snapshot_download(
        repo_id="OBLITERATUS/gemma-4-E4B-it-OBLITERATED",
        revision="main",          # or "q4_K_M" for quantized
        local_dir="/models/gemma4"
    )

if __name__ == "__main__":
    main()
