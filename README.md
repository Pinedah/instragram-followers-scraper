# Instagram Followers and Following Scraper

!! working on it... you can look at: instagram-photo-downloader meanwhile. !!


This repository contains a Python script that scrapes the list of followers and following from a given Instagram profile and exports the lists to either a PDF or TXT file, sorted alphabetically.

## Features

- **Scrape Followers & Following:** Extracts the list of followers and accounts the user is following.
- **Output Formats:** Saves the lists in either PDF or TXT format.
- **Sorting:** Automatically sorts the lists alphabetically.

## Requirements

- **Python 3.x**
- **Selenium**
- **ReportLab** (if exporting to PDF)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/instagram-scraper.git
   cd instagram-scraper
   
2. Install the required packages:
   -> Check the requirements section.

## Usage
   
1. Open the script and run it from terminal.
   ```bash
   python main.py

2. The script will open Instagram, then you need to log ig manually and go to the profile you want to scrap (it is necessary to have access to the profile).

3. Select the format [PDF or TXT] 

4. Te script will scrape the followers and following lists, sort them alphabetically, and then save them in the desired format.

5. By default, the lists will be saved in output.txt or output.pdf.

## Notes

- The script works for public profiles and for private profiles you follow.
- Ensure you comply with Instagram's terms of service when using this script.

## DISCLAIMER 

Script built with the only purpose to practice web scraping in python. Be aware.

Peace.




