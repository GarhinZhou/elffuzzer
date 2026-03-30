FROM aflplusplus/aflplusplus:latest

RUN sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list && \
    sed -i 's@//.*security.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
	python3 \
	patchelf \
	zstd

RUN cd / && git clone https://github.com/matrix1001/glibc-all-in-one.git
RUN pip install requests

RUN mkdir /input /output && chmod 777 /input /output

WORKDIR /elf

COPY elffuzzer /bin

CMD ["sleep", "infinity"]