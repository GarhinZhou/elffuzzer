# elffuzzer
afl++docker with glibc-all-in-one and patchelf
to fuzz elf more easily with patchelf and glibc-all-in-one in afl++docker

## Usage
1、Build the image: 

Navigate to the build directory and run build.sh to create the Docker image.

‘’‘
cd ./build
chmod +x ./build.sh
./build.sh
’‘’

2、Initialize the container: 

Run initdocker and provide the paths for your input (seeds) and output (crashes).

‘’‘
cd ../
chmod +x ./initdocker
./initdocker -i <inputpath> -o <outputpath>
’‘’

3、Enter the container: 

Execute startfuzz followed by the path to your ELF file.

‘’‘
./startfuzz /path/to/elf
’‘’

4、Access the shell: 

You will then be dropped into an interactive shell inside the AFL++ container.


5、Launch Fuzzing: 

Finally, run elffuzzer followed by the ELF path (typically /elf/your_binary) to begin AFL++ in QEMU mode.

‘’‘
elffuzzer /elf/your_elf
’‘’

You can use glibc-all-in-one and patchelf to patch your ELF binaries within the container.

However, please note that glibc-all-in-one requires root privileges to download the necessary library files.

‘’‘
docker exec -u 0 -it fuzzer bash
’‘’
