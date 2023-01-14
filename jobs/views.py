import json
import requests
from django.shortcuts import render
from .models import Job

class LatestJobsView(View):
    def get(self, request):
        # Fetch data from the HH API
        url = "https://api.hh.ru/vacancies"
        params = {
            "specialization": "1.221", # IT profession
            "date_from": "2022-12-01", # Past weekday in December
            "date_to": "2022-12-31",
            "per_page": 10,
            "sort": "publication_time"
        }
        response = requests.get(url, params=params)
        data = json.loads(response.text)

        # Create a list of Job objects from the fetched data
        jobs = []
        for item in data["items"]:
            job = Job(
                title=item["name"],
                description=item["description"],
                skills=",".join(item["key_skills"]),
                company=item["employer"]["name"],
                salary=item["salary"]["from"],
                region=item["area"]["name"],
                posted_date=item["published_at"]
            )
            jobs.append(job)

        # Pass the list of jobs to the template
        return render(request, "jobs/latest_jobs.html", {"jobs": jobs})
