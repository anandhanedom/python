from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, "lxml")

    # # print(soup.prettify())

    # first_course_tag = soup.find("h5")
    # print(first_course_tag)

    # courses_html_tags = soup.findAll("h5")
    # print(courses_html_tags)

    # for course in courses_html_tags:
    #     print(course.text)  # html tag text

    courses = soup.findAll("div", class_="card")

    for course in courses:
        course_name = course.h5.text
        course_price = course.a.text.split()[2]

        print(f"{course_name} costs {course_price}")
