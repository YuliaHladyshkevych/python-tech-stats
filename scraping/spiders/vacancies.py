import scrapy

from scrapy.http import Response


class VacanciesSpider(scrapy.Spider):
    name = "vacancies"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python", ]

    def parse(self, response: Response, **kwargs):

        for vacancy in response.css("div.job-list-item__title a::attr(href)").getall():
            yield response.follow(
                url=response.urljoin(vacancy),
                callback=self.parse_vacancies_from_page
            )

        next_page = response.css(
            ".pagination li.page-item.active + li.page-item a::attr(href)"
        ).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_vacancies_from_page(self, response: Response, **kwargs):
        title = response.css("h1::text").get().strip()
        company = response.css("a.job-details--title::text").get().strip()
        experience = int(
            response.css(
                'div.job-additional-info--item-text:contains("досвіду")::text'
            ).get().split()[0].replace("Без", "0")
        )
        salary = response.css(".public-salary-item::text").re_first(r"\$(\d+)")
        if salary:
            salary = int(salary)
        else:
            salary = None
        views = int(response.css("p.text-muted").re_first(r"(\d+) перегляд"))
        applications = int(response.css("p.text-muted").re_first(r"(\d+) відгук"))

        return {
            "title": title,
            "company": company,
            "experience": experience,
            "salary": salary,
            "views": views,
            "applications": applications,
        }
