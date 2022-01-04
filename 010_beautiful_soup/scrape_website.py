from bs4 import BeautifulSoup
import requests
import time

print("Enter some skill that you are not familiar with!")
unfamiliar_skill = input(">")
print(f"Filtering out {unfamiliar_skill}....")


def fetch_jobs():
    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    ).text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").span.text
        if "few" in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(
                " ", ""
            )
            required_skills = job.find("span", class_="srp-skills").text.replace(
                " ", ""
            )
            more_info = job.header.h2.a["href"]

            if unfamiliar_skill not in required_skills:

                with open(f"{index}.txt", "w") as new_file:

                    new_file.write(f"Company name: {company_name.strip()} \n")
                    new_file.write(f"Required skills: {required_skills.strip()} \n")
                    new_file.write(f"More info: {more_info} \n")
                    new_file.write("")
                print(f"File saved: {index}")


if __name__ == "__main__":
    while True:
        fetch_jobs()
        waiting_time = 10
        print(f"Waiting {waiting_time} minutes...")
        time.sleep(waiting_time * 60)
