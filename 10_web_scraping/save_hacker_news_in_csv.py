import csv
import requests
from bs4 import BeautifulSoup

hn_url = "https://news.ycombinator.com/news"
csv_file = "hacker_news.csv"


def get_hacker_news(url):
    headers = {"User-Agent": "MyCoolDataBot/1.0 (contact@example.com)"}

    try:
        response = requests.get(hn_url, timeout=10, headers=headers)
        response.raise_for_status()

    except requests.RequestException as e:
        print("some error occured : \n", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    stories = soup.select("span.titleline > a")
    posts = []
    for link in stories:
        title = link.text.strip()
        url = link.get("href")
        posts.append({"title": title, "url": url})
    # print(posts)
    return posts  # now this will return the array of dicts


def save_to_csv(posts):
    if not posts:
        print("Nothing to save")
        return
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url"])
        writer.writeheader()
        writer.writerows(posts)

    print(f"Saved Hacker News to {csv_file}")


def main():
    print("Scrapping the HN portal")
    posts = get_hacker_news(hn_url)
    print("Collected all data")
    save_to_csv(posts)


if __name__ == "__main__":
    main()
    # OUTPUT RECEIVED IS FROM STORIES IS :

# [<a href="https://alexxcons.github.io/blogpost_15.html">Xfwl4 – The Roadmap for a Xfce Wayland Compositor</a>, <a href="https://tonystr.net/blog/git_immitation">I made my own Git</a>, <a href="https://www.bbc.com/news/articles/c1evvx89559o">Heathrow scraps liquid container limit</a>, <a href="https://potch.me/2026/snow-simulation-toy.html">Snow Simulation Toy</a>, <a href="https://www.gutenberg.org/files/45109/45109-h/45109-h.htm">The Enchiridion by Epictetus</a>, <a href="https://github.com/velox-apps/velox">Velox: A Port of Tauri to Swift by Miguel de Icaza</a>, <a href="https://www.cnn.com/2026/01/26/tech/tiktok-ice-censorship-glitch-cec">TikTok users can't upload anti-ICE videos. The company blames tech issues</a>, <a href="https://tautvilas.medium.com/software-pump-and-dump-c8a9a73d313b">The age of Pump and Dump software</a>, <a href="https://telnet.org/htm/places.htm">A list of fun destinations for telnet</a>, <a href="https://lightwaves.io/en/eu-audit/">Show HN: We Built the 1. EU-Sovereignty Audit for Websites</a>, <a href="https://www.kimi.com/blog/kimi-k2-5.html">Kimi Released Kimi K2.5, Open-Source Visual SOTA-Agentic Model</a>, <a href="https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q" rel="nofollow">9 Mothers (YC X26, Defense Tech) Is Hiring</a>, <a href="item?id=46778461">Ask HN: Books to learn 6502 ASM and the Apple II</a>, <a href="https://consciousdigital.org/why-we-do-not-support-opt-out-forms/">We Do Not Support Opt-Out Forms (2025)</a>, <a href="https://www.apple.com/newsroom/2026/01/apple-introduces-new-airtag-with-expanded-range-and-improved-findability/">Apple introduces new AirTag with longer range and improved findability</a>, <a href="https://www.quantamagazine.org/in-mysterious-pattern-math-and-nature-converge-20130205/">The Universal Pattern Popping Up in Math, Physics and Biology (2013)</a>, <a href="https://nesbitt.io/2026/01/27/the-c-shaped-hole-in-package-management.html">The C-Shaped Hole in Package Management</a>, <a href="https://simonwillison.net/2026/Jan/26/chatgpt-containers/">ChatGPT Containers can now run bash, pip/npm install packages and download files</a>, <a href="https://practical.engineering/blog/2026/1/20/the-hidden-engineering-of-runways">The hidden engineering of runways</a>, <a href="https://www.windowscentral.com/microsoft/windows-11/windows-11s-botched-patch-tuesday-update-nightmare-continues-as-microsoft-confirms-some-pcs-might-fail-to-boot">Windows 11's Patch Tuesday nightmare gets worse</a>, <a href="https://www.greptile.com/blog/ai-code-review-bubble">There is an AI code review bubble</a>, <a href="https://www.iranintl.com/en/202601255198">Over 36,500 killed in Iran's deadliest massacre, documents reveal</a>, <a href="https://www.msn.com/en-us/news/technology/i-let-chatgpt-analyze-a-decade-of-my-apple-watch-data-then-i-called-my-doctor/ar-AA1UZxip">I let ChatGPT analyze a decade of my Apple Watch data, then I called my doctor</a>, <a href="https://nproject.io/blog/juicessh-give-me-back-my-pro-features/">JuiceSSH – Give me my pro features back</a>, <a href="https://buttondown.com/hillelwayne/archive/refinement-without-specification/">Refinement Without Specification</a>, <a href="https://www.zackliscio.com/posts/rip-low-code-2014-2025/">RIP Low-Code 2014-2025</a>, <a href="https://visualrambling.space/dithering-part-2/">Dithering – Part 2: The Ordered Dithering</a>, <a href="https://www.bbc.com/news/articles/c20gg729y1yo">Russia using Interpol's wanted list to target critics abroad, leak reveals</a>, <a href="https://arxiv.org/abs/2509.10846">New York Times games are hard: A computational perspective</a>, <a href="https://alexwennerberg.com/blog/2026-01-25-slop.html">AI code and software craft</a>]

# Now , we study the format of this output to modify it as per our desired format
