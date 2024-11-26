import re
from sentence_splitter import SentenceSplitter

def softsplit(text,lang):

    """
    
    Segments a text string twice, first using SentenceSplitter, and then with additional 
    segmentation for colons, semicolons, and other soft punctuation, such as quotations marks
    that SentenceSplitter will have missed. The aim is to provide a cleaner and more granular split 
    in order to yield smaller bitexts upon alignment.
    
    Args:
        text - string with text to split
        lang - language code
        
            Language codes include:
            
                Spanish - "es"
                English - "en"
                German - "de"
            
    Returns:
        segmented text as string

    """
 
    splitter = SentenceSplitter(language=lang)
    lines = splitter.split(text=text)
    lines = [sent.strip() for sent in lines if sent != ""]

    segmented_text = ""
    for line in lines:
        # Check if the line contains a URL
        if "http" in line:
            segmented_text += line + "\n"
            continue
        if len(line) == 0:
            continue

        # Split the line into words and punctuation
        words = re.split(r"([:;])", line)
        # Process each word and punctuation mark
        for word in words:
            if word in [":", ";"]:
                segmented_text += word + "\n"
            elif word.startswith("i.e."):
                segmented_text += word
            elif word.startswith("(") or word.startswith("["):
                segmented_text += word
            else:
                segmented_text += word + " "

        segmented_text += "\n"
        
    replacements = [
        (" :",":"),
        (" ;",";"),
        ("\n ","\n")
    ]
     
    for old, new in replacements:
        segmented_text = re.sub(old,new,segmented_text)
    
    # for German
    if lang == "de":
        while re.search("\w[.?!«] [„»]", segmented_text) != None:
            instance_lowcomma = re.search("\w[.?!«] [»„]", segmented_text)
            segmented_text = segmented_text[:instance_lowcomma.span()[0]+2]+"\n"+segmented_text[instance_lowcomma.span()[0]+3:]
            
        total_cases_endquote = re.findall("« [^a-z(]", segmented_text)
        for item in total_cases_endquote:
            instance_endquote = re.search(re.escape(item),segmented_text).span()[0]
            segmented_text = segmented_text[:instance_endquote+1]+"\n"+segmented_text[instance_endquote+2:]
    
    # for Spanish
    if lang == "es":
        while re.search("[.?!»] [—][A-Z¡¿].*\n", segmented_text) != None:
            instance_emdash = re.search("[.?!»] [—][A-Z¡¿].*\n", segmented_text)
            segmented_text = segmented_text[:instance_emdash.span()[0]+1]+"\n"+segmented_text[instance_emdash.span()[0]+2:] 

    segmented_text = re.sub("\n\n","\n",segmented_text)   

    additional_segments = len(segmented_text.split("\n")) - len(lines)
    print("Total additional segments:",additional_segments)
                   
    return segmented_text
