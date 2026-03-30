# elffuzzer
afl++docker with glibc-all-in-one and patchelf
to fuzz elf more easily with patchelf and glibc-all-in-one in afl++docker

## Usage
1、Build the image: 
Navigate to the build directory and run build.sh to create the Docker image.


2、Initialize the container: 
Run initdocker.sh and provide the paths for your input (seeds) and output (crashes).


3、Start the environment: 
Execute startfuzz followed by the path to your ELF file.


4、Access the shell: 
You will then be dropped into an interactive shell inside the AFL++ container.


5、Launch Fuzzing: 
Finally, run elffuzzer followed by the ELF path (typically /elf/your_binary) to begin AFL++ in QEMU mode.
