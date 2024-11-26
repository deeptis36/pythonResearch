import re
from datetime import datetime
from dateutil import parser

monthArr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
fullMonthArr = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def handle_skipped_dates(dates):
    
    # print("Date:", dates)
    tmppattern = r'\b([A-Za-z]{3})[’‘\'"]?(\d{2})\b'  # Pattern to match abbreviated month and 2-digit year

    # Find matches
    tmpdate = re.findall(tmppattern, dates)
    
    if tmpdate:
        month_abbr, year = tmpdate[0]  # Get the month and 2-digit year from the match
        # print("Matched Month and Year:", month_abbr, year)
        
        # Convert the month abbreviation to full month name
        if month_abbr in monthArr:
            month_full = fullMonthArr[monthArr.index(month_abbr)]
            # print("Full Month Name:", month_full)
        else:
            # print("Invalid month abbreviation.")
            return None
        
        # Convert the 2-digit year to 4-digit year
        year = "20" + year if int(year) < 50 else "19" + year  # Adjust century based on the year
        # print("Full Year:", year)

        # Return or format as needed

        return f"{month_abbr} {year}"
    else:
        print("No valid date found.")
        return dates



import re
from datetime import datetime
from dateutil import parser

def extract_dates(text):
    """
    Extracts all date ranges from the text, handling various formats.
    If "TILL DATE" or similar phrases are found, consider today's date.

    Parameters:
        text (str): The input text containing dates.

    Returns:
        list: A list of extracted date ranges or individual dates in 'Month YYYY' format.
    """
    # List of phrases indicating the current date should be used
    current_phrases = ["TILL DATE", "at present", "currently working", "Present"]
    
    # Regular expression to match various date formats (month-year ranges and individual dates)
    range_patterns = [
        r'(\b(?:[A-Za-z]{3,9} \d{4})\b)\s*–\s*(\b(?:[A-Za-z]{3,9} \d{4})\b)',  # "Feb 2023 – Jul 2023"
        r'(\b(?:[A-Za-z]{3}\/\d{4})\b)\s*-\s*(\b(?:[A-Za-z]{3}\/\d{4})\b)',     # "Feb/2023-Jul/2023"
        r'(\b(?:\d{2}\.\d{4})\b)\s*-\s*(\b(?:\d{2}\.\d{4})\b)',                 # "02.2023-17.2023"
        r'(\b(?:\d{2}\/\d{4})\b)\s*-\s*(\b(?:\d{2}\/\d{4})\b)',                 # "02/2023-17/2023"
    ]
    
    dates = []
    
    # Check if the text contains any of the "current" phrases and handle it
    if any(phrase in text for phrase in current_phrases):
        today = datetime.today().strftime('%b %Y')  # Get today's date in 'Month YYYY' format
        for phrase in current_phrases:
            text = text.replace(phrase, today)  # Replace any "current" phrase with today's date

    # Extract date ranges using multiple patterns
    for pattern in range_patterns:
        matches = re.findall(pattern, text)
       
        for start_date, end_date in matches:
            try:
                # Normalize to 'Month YYYY' format
                start_parsed = parser.parse(start_date.replace("/", " ").replace(".", " ")).strftime('%b %Y')
                end_parsed = parser.parse(end_date.replace("/", " ").replace(".", " ")).strftime('%b %Y')
                dates.extend([start_parsed, end_parsed])
            except Exception as e:
                print(f"Error parsing date: {e}")

    # Optionally, extract individual dates (if needed)
    individual_dates = re.findall(r'\b(?:\d{2}\/\d{4}|\w{3,9} \d{4}|\d{4}-\d{2}-\d{2})\b', text)
    for date_str in individual_dates:
        try:
            parsed_date = parser.parse(date_str)
            dates.append(parsed_date.strftime('%b %Y'))  # Standardize to 'Month YYYY' format
        except ValueError:
            pass  # Ignore invalid date formats

    return dates


# # Example usage
# text = "I worked at XYZ from February 2023 – July 2023, and previously from 02.2023-17.2023 to 05/2021-10/2022. Also worked in Sep ’15 – Aug ‘20."
# result = extract_dates(text)

# # Print the result
# print("Extracted Dates:", result)
