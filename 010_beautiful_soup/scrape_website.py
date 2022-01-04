from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
).text

# print(html_text)

soup = BeautifulSoup(html_text, "lxml")

# job = soup.find("li", class_="clearfix job-bx wht-shd-bx")
# company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
# skills = job.find("span", class_="srp-skills").text.replace(" ", "")
# published_date = job.find("span", class_="sim-posted").span.text

# print(published_date)

# print(company_name)
# print(skills)


# print(f"Company name: {company_name}")
# print(f"Required skills: {skills}")


jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    published_date = job.find("span", class_="sim-posted").span.text
    if "few" in published_date:
        company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
        required_skills = job.find("span", class_="srp-skills").text.replace(" ", "")

        print(f"Company name: {company_name.strip()}")
        print(f"Required skills: {required_skills.strip()}")
        print("")
