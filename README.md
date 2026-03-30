# elffuzzer
afl++docker with glibc-all-in-one and patchelf
to fuzz elf more easily with patchelf and glibc-all-in-one in afl++docker

## Usage
Build the image: Navigate to the build directory and run build.sh to create the Docker image.

Initialize the container: Run initdocker.sh and provide the paths for your input (seeds) and output (crashes).

Start the environment: Execute startfuzz followed by the path to your ELF file.

Access the shell: You will then be dropped into an interactive shell inside the AFL++ container.

Launch Fuzzing: Finally, run elffuzzer followed by the ELF path (typically /elf/your_binary) to begin AFL++ in QEMU mode.
