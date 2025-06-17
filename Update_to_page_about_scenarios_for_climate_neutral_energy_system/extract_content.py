#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "beautifulsoup4",
#     "lxml",
# ]
# ///

import re
from bs4 import BeautifulSoup
from pathlib import Path

def extract_main_content(html_file):
    """Extract the main content from TNO website HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
    
    # Remove script and style tags
    for script in soup(["script", "style"]):
        script.decompose()
    
    # Find main content area (usually in article or main tags)
    main_content = soup.find('main') or soup.find('article') or soup.find('div', {'class': re.compile('content|main', re.I)})
    
    if not main_content:
        # Fallback to body content
        main_content = soup.body
    
    # Extract headings and paragraphs
    content_sections = []
    
    for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol']):
        if element.name.startswith('h'):
            content_sections.append({
                'type': 'heading',
                'level': int(element.name[1]),
                'text': element.get_text(strip=True)
            })
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text:
                content_sections.append({
                    'type': 'paragraph',
                    'text': text
                })
        elif element.name in ['ul', 'ol']:
            items = [li.get_text(strip=True) for li in element.find_all('li')]
            if items:
                content_sections.append({
                    'type': 'list',
                    'ordered': element.name == 'ol',
                    'items': items
                })
    
    return content_sections

def save_structured_content(content_sections, output_file):
    """Save the structured content to a markdown file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for section in content_sections:
            if section['type'] == 'heading':
                f.write(f"\n{'#' * section['level']} {section['text']}\n\n")
            elif section['type'] == 'paragraph':
                f.write(f"{section['text']}\n\n")
            elif section['type'] == 'list':
                for item in section['items']:
                    prefix = '1.' if section['ordered'] else '-'
                    f.write(f"{prefix} {item}\n")
                f.write('\n')

# Process English version
english_content = extract_main_content('./downloads/tno_scenarios_english.html')
save_structured_content(english_content, './downloads/tno_content_english_extracted.md')

# Process Dutch version
dutch_content = extract_main_content('./downloads/tno_scenarios_dutch.html')
save_structured_content(dutch_content, './downloads/tno_content_dutch_extracted.md')

print("Content extraction completed!")
print(f"English sections: {len(english_content)}")
print(f"Dutch sections: {len(dutch_content)}")