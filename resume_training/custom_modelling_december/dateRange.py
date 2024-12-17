import re

def extract_date_ranges(text):
    """
    Extract date ranges from the input text.
    Supports various formats like 'January 2019 - December 2020', '2019 - 2020', etc.
    """
    # Define the regex for date ranges
    daate_pattern = r"""
        (\b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?\s?\d{4})  # Optional short month and year
        \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
        (\b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?\s?\d{4}|Present|till\s?date)  # Optional short month and year or 'Present'
    """

    date_pattern = r"""
        (\b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4})  # Month and year (e.g., Nov 2022)
        \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
        (\b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}|Present|till\s?date|Till\s?Date)  # Month and year or 'Present' or 'Till date'
    """
    date_pattern = r"""
        (\b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4})  # Month and year (e.g., Nov 2022)
        \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
        (\b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}|Present|till\s?date)  # Month and year or 'Present' or 'Till date'
    """
    date_pattern = r"""
        (\b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4})  # Month and year (e.g., Nov 2022)
        \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
        (\b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}|Present|till\s?date)  # Month and year or 'Present' or 'Till date'
    """
    date_pattern = r"""
    (\b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
    Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4})  # Month and year (e.g., Nov 2022)
    \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
    (\b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
    Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}|Present|Till\s?Date|till\s?date)  # Month and year, 'Present', 'Till Date'
"""

    date_pattern = r"""
        (\b\d{2}/\d{4})  # Starting month/year (e.g., 04/2018)
        \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
        (\b\d{2}/\d{4}|Present|Till\s?Date|till\s?date)  # Ending month/year or 'Present', 'Till Date'
    """

    date_pattern = r"""
    (
        \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}  # Month and year (e.g., Nov 2022)
        |
        \b\d{2}/\d{4}  # MM/YYYY (e.g., 04/2018)
    )
    \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
    (
        \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}  # Month and year (e.g., Nov 2022)
        |
        \b\d{2}/\d{4}  # MM/YYYY (e.g., 04/2018)
        |
        Present|Till\s?Date|till\s?date  # 'Present' or 'Till Date'
    )
"""



    date_pattern = r"""
        (
            \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
            Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}  # Month and year (e.g., Nov 2022)
            |
            \b\d{2}/\d{4}  # MM/YYYY (e.g., 04/2018)
        )
        \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
        (
            \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
            Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}  # Month and year (e.g., Nov 2022)
            |
            \b\d{2}/\d{4}  # MM/YYYY (e.g., 04/2018)
            |
            Present|Till\s?Date|till\s?date  # 'Present' or 'Till Date'
        )
    """

    date_pattern = r"""
        (
            \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
            Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}  # Month and year (e.g., Nov 2022)
            |
            \b\d{2}/\d{4} | # MM/YYYY (e.g., 04/2018)
            \b\d{1}/\d{2}  # MM/YYYY (e.g., 04/2018)
        )
        \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
        (
            \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
            Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}  # Month and year (e.g., Nov 2022)
            |
            \b\d{2}/\d{4}  # MM/YYYY (e.g., 04/2018)
            |
            Present|Till\s?Date|till\s?date  # 'Present' or 'Till Date'
        )
    """
    date_pattern = r"""
        (
            \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
            Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}  # Month and year (e.g., Nov 2022)
            |
            \b\d{2}/\d{4}  # MM/YYYY (e.g., 04/2018)
            |
            \b\d{1,2}/\d{2}  # MM/YY (e.g., 4/98, 04/00)
        )
        \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
        (
            \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
            Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}  # Month and year (e.g., Nov 2022)
            |
            \b\d{2}/\d{4}  # MM/YYYY (e.g., 04/2018)
            |
            \b\d{1,2}/\d{2}  # MM/YY (e.g., 4/98, 04/00)
            |
            Present|Till\s?Date|till\s?date  # 'Present' or 'Till Date'
        )
    """

    date_pattern = r"""
        (
            \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
            Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}  # Month and year (e.g., Nov 2022)
            |
            \b\d{2}/\d{4}  # MM/YYYY (e.g., 04/2018)
            |
            \b\d{1,2}/\d{2}  # MM/YY (e.g., 4/98, 04/00)
            |
            \b\d{4}  # Single year (e.g., 2023)
        )
        \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
        (
            \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
            Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{4}  # Month and year (e.g., Nov 2022)
            |
            \b\d{2}/\d{4}  # MM/YYYY (e.g., 04/2018)
            |
            \b\d{1,2}/\d{2}  # MM/YY (e.g., 4/98, 04/00)
            |
            \b\d{4}  # Single year (e.g., 2023)
            |
            Present|Till\s?Date|till\s?date  # 'Present' or 'Till Date'
        )
    """
    date_pattern = r"""
    (
        \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|
        january|february|march|april|may|june|july|august|september|october|november|december|  # Lowercase full month names
        jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)  # Lowercase short month names
        ,?\s?\d{4}  # Optional comma and the year (e.g., May, 2019 or may 2019)
    )
    \s?[–\-~to]+\s?  # Separator: dash, en-dash, tilde, or 'to'
    (
        \b(?:January|February|March|April|May|June|July|August|September|October|November|December|  # Full month names
        Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|
        january|february|march|april|may|june|july|august|september|october|november|december|  # Lowercase full month names
        jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)  # Lowercase short month names
        ,?\s?\d{4}  # Optional comma and the year (e.g., August, 2020 or august 2020)
        |
        Present|Till\s?Date|till\s?date  # 'Present' or 'Till Date'
    )
    """


    # Use re.findall to get all matches
   
    matches = re.findall(date_pattern, text, re.IGNORECASE | re.VERBOSE)
    
    # Clean the matches to form date ranges
    date_ranges = [f"{start} - {end}" for start, end in matches]
    # print("_"*80)
    # print(text)
    # print(date_ranges)
    # print("_"*80)
    return date_ranges
    
