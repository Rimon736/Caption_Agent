import yake

def extract_keywords(text, max_ngram_size=2, num_keywords=15):
    """
    Extracts 10-15 high-value keywords using YAKE[cite: 18].
    """
    # Initialize YAKE
    kw_extractor = yake.KeywordExtractor(
        lan="en", 
        n=max_ngram_size, 
        dedupLim=0.9, 
        top=num_keywords, 
        features=None
    )
    
    # Extract keywords
    keywords = kw_extractor.extract_keywords(text)
    
    # Clean up the output (YAKE returns scores, we just want the words)
    # Lower score = higher relevance in YAKE, but we just list them here.
    clean_keywords = [kw[0] for kw in keywords]
    
    return clean_keywords