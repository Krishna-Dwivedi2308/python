import requests
import threading
import time


def download(url, filename):

    print(f"starting download fro {url}")
    try:
        resp = requests.get(url=url, stream=True)
        resp.raise_for_status()
        # write to disk
        with open(filename, "wb") as f:
            for chunk in resp.iter_content(8192):
                f.write(chunk)
    except Exception as e:
        print("Something went wrong: ", e)
        # print(f"Finished downloading from {url} , size : {len(resp.content)} bytes")


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = (
    []
)  # so that we can store them and join them later by iterating over this array
count = 1
for url in urls:
    ext = url.split("/")[-1]
    filename = f"C:/Users/krish/Desktop/python hitesh/13_threads_concurrency/Downloads/image{count}.{ext}"
    t = threading.Thread(target=download, args=(url, filename))
    count += 1
    t.start()
    threads.append(t)


for t in threads:
    t.join()

end = time.time()
print(f"the time taken to complete the entire process is {end-start:.2f} seconds")
