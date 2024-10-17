from bs4 import BeautifulSoup

def get_employer_info(soup):
    employers_info = []
    # Find all employer cards
    employer_cards = soup.find_all("div", {"data-bind": "react_component: { name: 'RegistrationsCardRoot', props: $data }"})
    
    for card in employer_cards:
        # Extract employer name
        employer_name = card.find("h2", class_="style__heading___29i1Z style__large___15W-p style__fitted___3L0Tr").text.strip()

        # Extract location
        location = card.find("div", class_="fa-map-marker-alt").find_next("div").text.strip() if card.find("div", class_="fa-map-marker-alt") else None

        # Extract job types (e.g., Full-time, Internship)
        job_type = card.find("div", class_="style__section-header___xP0ED", text="Job Type").find_next("div").text.strip() if card.find("div", class_="style__section-header___xP0ED", text="Job Type") else None

        # Extract employment type (e.g., Full-Time, Part-Time)
        employment_type = card.find("div", class_="style__section-header___xP0ED", text="Employment Type").find_next("div").text.strip() if card.find("div", class_="style__section-header___xP0ED", text="Employment Type") else None

        # Extract website URL
        website = card.find("a", href=True).get('href') if card.find("a", href=True) else None

        # Store the info in a dictionary (JSON-like object)
        employer_data = {
            "employer_name": employer_name,
            "location": location,
            "job_type": job_type,
            "employment_type": employment_type,
            "website": website
        }

        employers_info.append(employer_data)
    
    return employers_info