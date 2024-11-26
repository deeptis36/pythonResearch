from pdfminer.high_level import extract_text
 
import re
import subprocess  
 
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
 
 
def doc_to_text_catdoc(file_path):
    try:
        process = subprocess.Popen(  
            ['resume.pdf', '-w', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
    except (
        FileNotFoundError,
        ValueError,
        subprocess.TimeoutExpired,
        subprocess.SubprocessError,
    ) as err:
        return (None, str(err))
    else:
        stdout, stderr = process.communicate()
 
    return (stdout.strip(), stderr.strip())
 
 
def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)
 
    if phone:
        number = ''.join(phone[0])
 
        if resume_text.find(number) >= 0 and len(number) <16:
            return number
    return None
 
 
if __name__ == '__main__':
    text = doc_to_text_catdoc('resume.pdf')
    print(text)
    # phone_number = extract_phone_number(text)
 
    # print(phone_number)